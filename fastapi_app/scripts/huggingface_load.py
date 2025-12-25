"""Hugging Face utilities for downloading ML models."""

import os
import logging
from transformers import AutoImageProcessor, AutoModelForImageClassification
from huggingface_hub.utils import RepositoryNotFoundError

logger = logging.getLogger(__name__)

HF_MODEL_ID = "codeby-hp/finetune-VIT-HumanPoseClassification"


def download_model_from_huggingface(local_path: str) -> bool:
    """Download model from Hugging Face Hub.
    
    Args:
        local_path: Local directory path to save model
        
    Returns:
        True if successful, False otherwise
    """
    try:
        logger.info(f"Downloading model from Hugging Face: {HF_MODEL_ID}")
        os.makedirs(local_path, exist_ok=True)
        
        # Download image processor
        logger.info("Downloading image processor...")
        image_processor = AutoImageProcessor.from_pretrained(
            HF_MODEL_ID,
            cache_dir=local_path,
        )
        image_processor.save_pretrained(local_path)
        
        # Download model
        logger.info("Downloading model weights...")
        model = AutoModelForImageClassification.from_pretrained(
            HF_MODEL_ID,
            cache_dir=local_path,
        )
        model.save_pretrained(local_path)
        
        logger.info(f"Successfully downloaded model to {local_path}")
        return True
        
    except RepositoryNotFoundError as e:
        logger.error(f"Model not found on Hugging Face Hub: {e}")
        return False
    except Exception as e:
        logger.error(f"Error downloading model from Hugging Face: {e}")
        return False
