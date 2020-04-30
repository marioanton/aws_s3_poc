#!/usr/bin/env python

# Import MinIO library.
from minio import Minio
from minio.error import ResponseError
import sys, traceback

def s3_auth_and_access():
    print("Authenticating with S3")

    minioClient = Minio('127.0.0.1:9000',
       access_key='minioadmin',    # Credentials to be exported to config file
       secret_key='minioassdmin',  # Credentials to be exported to config file
       secure=False)

    # Make a list bucket with the list_buckets API call.
    try:
        minioClient.list_buckets()  # no need to show existing buckets, just to verify the capabilities of auth and access.
    except ResponseError as err:
        raise
        sys.exit()


