import io
import boto3
import pandas as pd

class S3DataService:
    def __init__(self, endpoint_url, access_key, secret_key, bucket_name):
        self.client = boto3.client(
            's3',
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        self.bucket_name = bucket_name

    def read_excel(self, key, **kwargs):
        response = self.client.get_object(Bucket=self.bucket_name, Key=key)
        return pd.read_excel(io.BytesIO(response['Body'].read()), **kwargs)