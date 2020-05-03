#!/usr/bin/env python
import boto3
import botocore
import subprocess

def s3_get_object(client):
    print("Get Obj")
    # s3.Object("maylogs",'my/key/including/anotherfilename.txt')
    client.get_object()

def s3_get_bucket(client):
    # session= boto3.client.se
    print("Get Obj")
    response= (client.list_objects(
        Bucket='maylogs',
        MaxKeys=23
    ))
    print(len(response["Contents"]))
    # This returns 1000 as max so would iterate and delete when file proved is migrated

def s3_del_objects(client, object):

    print("Delete Object")

def s3_set_object(client):
    print("Set Obj")
    some_binary_data = b'Here we have some data'
    for x in range(3000):
        client.put_object(Body=some_binary_data, Bucket="maylogs", Key="legacy/image%d.png" % x) 
    # print(client.get_object( Bucket='maylogs', Key='my/key/including/anotherfilename.txt'))
    # add privs in here to be readable by anyone

def s3_update_object(client):
    print("Set Obj")

def s3_sync(endpoint, src_bucket, dst_bucket ):
    print( "Starting Sync")
    cmd = "aws s3 sync s3://%s s3://%s --endpoint-url=%s"  % (src_bucket, dst_bucket, endpoint)
    try:
        subprocess.call(cmd, shell=True)
        print( "Sync Done")
    except subprocess.CalledProcessError as e:
        print(e.output)
        sys.exit(1)

def s3_object_rename(client, dst_bucket, legacy_key, production_key):
    
    # print(object_name)
    # print(dst_key)
        # client.put_object(Body=some_binary_data, Bucket="maylogs", Key="legacy/image%d.png" % x) 
    try:
        bucket_and_key = "%s/%s" %(dst_bucket,legacy_key)
        client.copy_object(Bucket=dst_bucket, CopySource=bucket_and_key, Key=production_key )
    except botocore.exceptions.ClientError as error:
        # Put your error handling logic here
        raise error 
        sys.exit(1)

def s3_object_delete(client, dst_bucket, legacy_key, production_key):
    print("delete stuff")