#The boto3 library for handling data on AWS 
import boto3

s3 = boto3.client('s3',
                  aws_access_key_id="YOUR_AWS_ACCESS_KEY", #Place here 
                  aws_secret_access_key="YOUR_AWS_SECRET_KEY",#Put here 
                  region_name="us-east-1")
BUCKET_NAME = "your-bucket-name" #Name your bucket 

#A function for saving and sending data to the cloud. 
def upload_to_s3(content, filename):
    if isinstance(content, str) and content.endswith(".txt"):
        s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=content)
    else:
        with open(content, "rb") as f:
            s3.upload_fileobj(f, BUCKET_NAME, filename)
    return f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
