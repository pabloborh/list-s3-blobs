from os import environ
from flask import Flask, json
from boto3 import client
from boto3 import Session


def getS3Client():
# Eslablish sessin with AWS
    print("Establishing session using AK and SK...")
    session = Session(
        aws_access_key_id=environ['AWS_ACCESS_KEY'],
        aws_secret_access_key=environ['AWS_SECRET_ACCESS_KEY'],
    )
    s3_client = session.client('s3')
    
    return s3_client

def getS3Objects():
# Retrieve objects from bucket
    s3_client = getS3Client()

    list_objects = s3_client.list_objects_v2(Bucket=environ['AWS_BUCKET'])

    if 'Contents' not in list_objects:
        print('There are no objects in '+ environ['AWS_BUCKET'])
        return []

    s3_files = []

    for key in list_objects['Contents']:
        s3_files.append(key['Key'])

    while list_objects['IsTruncated']:
        
        next_continuation_token = list_objects['NextContinuationToken']
        list_objects = list_objects = s3_client.list_objects_v2(Bucket=environ['AWS_BUCKET'], ContinuationToken=next_continuation_token)
        
        for key in list_objects['Contents']:
            s3_files.append(key['Key'])

    return s3_files

def main():

    api = Flask(__name__)
    
    #Establish /list endpoint
    @api.route('/list', methods=['GET'])
    def get_list():
        s3_files=getS3Objects()
        return json.dumps(s3_files)

    if __name__ == '__main__':
        api.run() 

main()