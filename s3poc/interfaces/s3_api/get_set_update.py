#!/usr/bin/env python
import boto3
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

def s3_update_metadata(client):
    bucket = "maylogs"
    key = "my/key/including/anotherfilename2.txt"
    k = client.head_object(Bucket = bucket, Key = key)
    m = k["Metadata"]
    m["moved"] = "no"
    # client.copy_object(Bucket = bucket, Key = key, CopySource = bucket + '/' + key, Metadata = m, MetadataDirective='REPLACE')

def s3_sync(endpoint, src_bucket, dst_bucket ):
    print( "Starting Sync")
    cmd = "aws s3 sync s3://%s s3://%s --endpoint-url=%s"  % (src_bucket, dst_bucket, endpoint)
    subprocess.call(cmd, shell=True)
    print( "Time Taken")


def s3_object_rename(client, dst_bucket, legacy_key, production_key):
    
    # print(object_name)
    # print(dst_key)
        # client.put_object(Body=some_binary_data, Bucket="maylogs", Key="legacy/image%d.png" % x) 
    bucket_and_key = "%s/%s" %(dst_bucket,legacy_key)
    client.copy_object(Bucket=dst_bucket, CopySource=bucket_and_key, Key=production_key )

def s3_object_delete(client, dst_bucket, legacy_key, production_key):
    print("delete stuff")

