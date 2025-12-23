"""Data models for pose classification API."""

from pydantic import BaseModel, Field


class PoseClassificationRequest(BaseModel):
    """Request body for pose classification endpoint."""
    url: str = Field(
        description="Image URL for classification"
    )


class PosePrediction(BaseModel):
    """Single pose prediction result."""
    label: str
    score: float


class PoseClassificationResponse(BaseModel):
    """Response body for pose classification endpoint."""
    model_name: str = "vit-human-pose-classification"
    prediction: PosePrediction
    prediction_time_ms: int = Field(
        description="Time taken for inference in milliseconds"
    )





