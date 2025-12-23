"""S3 utilities for downloading ML models."""

import boto3
import os
import logging
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

logger = logging.getLogger(__name__)

bucket_name = os.getenv("AWS_BUCKET_NAME")
if not bucket_name:
    logger.warning("AWS_BUCKET_NAME environment variable not set")

try:
    s3_client = boto3.client("s3")
except Exception as e:
    logger.error(f"Failed to initialize S3 client: {e}")
    s3_client = None


def download_model_from_s3(local_path: str, model_name: str) -> bool:
    """Download model directory from S3.
    
    Args:
        local_path: Local directory path to save model
        model_name: Model name/prefix in S3 bucket
        
    Returns:
        True if successful, False otherwise
    """
    if not s3_client or not bucket_name:
        logger.error("S3 client not initialized or bucket name not configured")
        return False

    try:
        s3_prefix = f"ml-models/{model_name}"
        os.makedirs(local_path, exist_ok=True)
        
        paginator = s3_client.get_paginator("list_objects_v2")
        page_iterator = paginator.paginate(
            Bucket=bucket_name, Prefix=s3_prefix
        )
        
        for page in page_iterator:
            if "Contents" not in page:
                continue
                
            for obj in page["Contents"]:
                s3_key = obj["Key"]
                local_file = os.path.join(
                    local_path, os.path.relpath(s3_key, s3_prefix)
                )
                
                os.makedirs(os.path.dirname(local_file), exist_ok=True)
                logger.info(f"Downloading {s3_key} to {local_file}")
                s3_client.download_file(bucket_name, s3_key, local_file)
        
        logger.info(f"Successfully downloaded model from {s3_prefix}")
        return True
        
    except ClientError as e:
        logger.error(f"S3 client error: {e}")
        return False
    except Exception as e:
        logger.error(f"Error downloading model: {e}")
        return False
