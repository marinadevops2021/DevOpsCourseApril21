import boto3
from botocore.exceptions import ClientError
client = boto3.client('iam')

def create_user(username,client):
    """
    Create a user "username" with an appropriate permissions (S3VideoReader you've just created)
    """
    try:
        response = client.create_user(
            UserName= username,
            PermissionsBoundary='arn:aws:iam::955114013936:policy/S3VideoReader',
            Tags=[
                {
                    'Key': 'YoutubeAppSub',
                    'Value': '1'
                },
            ]
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("User already exists")
        else:
            print("Unexpected error: %s" % e)

