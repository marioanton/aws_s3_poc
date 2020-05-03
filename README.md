# sk - aws_s3_poc

This is mean to be a small program to do some specific tasks related to S3 storage operations.

Requirements:

1. python 3.8.2. I started using [pyenv](https://github.com/pyenv/pyenv) to avoid issues with versioning.
2. boto and minio library (minio to be decommmisioned, just does testing on auth)
3. docker container for minio s3 emulation. [minio](https://github.com/minio/minio)
4. docker container for mysql.

Assumptions:
1. Both S3 in the same region, would use s3 vpc endpoints to reach internally and reduce bandwith issues and speed up the transfer.
2. .aws config files are in place already with proper configs

This project is for a POC and intends to:

- Will copy/move image files from one S3 bucket to another. One-off operation.
- Will update database table to reflect image files are available in destination S3 bucket.
- Will perform tests before updating the database table.
- Will aim to get the best perfomance for the given operation.
- Will enable users to run as much times as required to finish the operation.

How this should work.

- Initial sync is done. This can take loads of time depending on the number of objects. 
    - Perfomance can be improved by setting this: https://aws.amazon.com/premiumsupport/knowledge-center/s3-improve-transfer-sync-command/
- Iterates a limit of 100 elements within the db
    - Performs operations to check whether the file was synced and is accesible.
    - Renames the object key path
    - Updates DB table
