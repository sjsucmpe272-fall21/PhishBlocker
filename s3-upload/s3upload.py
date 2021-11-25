import boto3
import botocore

BUCKET_NAME = 'my-bucket' # replace with your bucket name
KEY = 'my_image_in_s3.jpg' # replace with your object key

s3 = boto3.resource('s3','s3',aws_access_key_id='AKIASXDB4DJBSZNISVLC',
aws_secret_access_key='2QcOqt83rwXd6e8iuNj')

try:
    s3.Bucket(BUCKET_NAME).download_file('img_618ff6d8f70eb0682ae3882b', 'my_local_image.jpg')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise