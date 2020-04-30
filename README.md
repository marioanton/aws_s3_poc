# sk - aws_s3_poc

This is mean to be a small program to do some specific tasks related to S3 storage operations.

Requirements:

1. python 3.8.2. I started using [pyenv](https://github.com/pyenv/pyenv) to avoid issues with versioning.
2. minio library (pip install -r requirements.txt)
3. docker container for minio s3 emulationgit a
4. pillow python module for images generation

This project is for a POC and intends to:

- Will copy/move image files from one S3 bucket to another. One-off operation.
- Will update database table to reflect image files are available in destination S3 bucket.
- Will perform tests before updating the database table.
- Will verify old files are not being accessed ?
- Will aim to get the best perfomance for the given operation.
- Will enable users to run as much times as required to finish the operation.

Assumptions:

- New image files are written to destination S3 bucket. No new image files are uploaded to the source S3 bucket.
