import logging
import os
import time
import warnings
from pathlib import Path

import torch
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from transformers import AutoImageProcessor, pipeline
from PIL import Image
import io

from scripts.data_model import (
    PoseClassificationResponse,
    PosePrediction,
)
from scripts.s3 import download_model_from_s3
from scripts.huggingface_load import download_model_from_huggingface

# Toggle between S3 and Hugging Face model loading
# Set USE_HUGGINGFACE_MODELS = False to use S3 loader (production)
# Set USE_HUGGINGFACE_MODELS = True to use Hugging Face loader (Spaces deployment)
USE_HUGGINGFACE_MODELS = False

warnings.filterwarnings("ignore")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Pose Classification API",
    description="ViT-based human pose classification service",
    version="0.0.0",
)

# Setup templates
template_dir = Path(__file__).parent / "templates"
if template_dir.exists():
    templates = Jinja2Templates(directory=str(template_dir))

# Device selection
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
logger.info(f"Using device: {device}")

# Model initialization
MODEL_NAME = "vit-human-pose-classification"
LOCAL_MODEL_PATH = f"ml-models/{MODEL_NAME}"
FORCE_DOWNLOAD = False

# Global model variables
pose_model = None
image_processor = None


def initialize_model():
    """Initialize the pose classification model."""
    global pose_model, image_processor
    
    try:
        logger.info("Initializing pose classification model...")
        
        # Download model if not present
        if not os.path.isdir(LOCAL_MODEL_PATH) or FORCE_DOWNLOAD:
            if USE_HUGGINGFACE_MODELS:
                logger.info(f"Downloading model from Hugging Face to {LOCAL_MODEL_PATH}")
                success = download_model_from_huggingface(LOCAL_MODEL_PATH)
            else:
                logger.info(f"Downloading model from S3 to {LOCAL_MODEL_PATH}")
                success = download_model_from_s3(LOCAL_MODEL_PATH, f"{MODEL_NAME}/")
            
            if not success:
                logger.error("Failed to download model")
                return False
        
        # Load image processor
        image_processor = AutoImageProcessor.from_pretrained(
            LOCAL_MODEL_PATH,
            use_fast=True,
            local_files_only=True,
        )
        
        # Load model pipeline
        pose_model = pipeline(
            "image-classification",
            model=LOCAL_MODEL_PATH,
            device=device,
            image_processor=image_processor,
        )
        
        logger.info("Model initialized successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error initializing model: {e}")
        return False


@app.on_event("startup")
async def startup_event():
    """Initialize model on startup."""
    if not initialize_model():
        logger.warning("Model initialization failed, app will not be fully functional")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main UI page."""
    if template_dir.exists():
        return templates.TemplateResponse("index.html", {"request": request})
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Pose Classification</title></head>
    <body><p>Template not found</p></body>
    </html>
    """


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    if pose_model is not None:
        return {"status": "healthy", "model_loaded": True}
    return {"status": "unhealthy", "model_loaded": False}


@app.post("/api/v1/classify")
async def classify_pose(file: UploadFile = File(...)) -> PoseClassificationResponse:
    """Classify pose from uploaded image.
    
    Args:
        file: Image file to classify
        
    Returns:
        PoseClassificationResponse with prediction results
    """
    if pose_model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please try again later.",
        )
    
    try:
        # Read and validate image
        content = await file.read()
        image = Image.open(io.BytesIO(content))
        
        # Run inference
        start_time = time.time()
        output = pose_model(image)
        inference_time = int((time.time() - start_time) * 1000)
        
        # Extract top prediction
        top_prediction = output[0]
        
        return PoseClassificationResponse(
            prediction=PosePrediction(
                label=top_prediction["label"],
                score=round(top_prediction["score"], 4),
            ),
            prediction_time_ms=inference_time,
        )
        
    except Exception as e:
        logger.error(f"Error during inference: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"Error processing image: {str(e)}",
        )
    
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app="app:app", port=8000, reload=True, host="0.0.0.0")
