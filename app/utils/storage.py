import os
import boto3
from botocore.exceptions import BotoCoreError
from app.config import settings

def save_file_locally(file_path: str):
    # Files are already saved in download service
    return file_path

def upload_to_s3(local_path: str, key: str):
    if not settings.AWS_S3_BUCKET:
        raise ValueError("S3 bucket not configured")
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
    )
    try:
        s3.upload_file(local_path, settings.AWS_S3_BUCKET, key)
    except BotoCoreError as e:
        raise RuntimeError(f"S3 upload failed: {e}")
    return key

def generate_presigned_url(key: str, expires_in=3600):
    if not settings.AWS_S3_BUCKET:
        raise ValueError("S3 bucket not configured")
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
    )
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": settings.AWS_S3_BUCKET, "Key": key},
        ExpiresIn=expires_in,
    )

def delete_local_file(path: str):
    try:
        os.remove(path)
    except OSError:
        pass
