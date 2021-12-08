import boto3
access_key = "AKIAVWYJVEF6PK5KS74W"
secret_key = "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"
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
s3.download_file('phishblocker-model', 'model.joblib', '/home/ubuntu/ML/model.joblib')
