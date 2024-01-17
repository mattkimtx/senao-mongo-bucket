import boto3
from dotenv import load_dotenv
import os

load_dotenv()

session = boto3.Session(
     region_name="us-west-2",
     aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
     aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)

class Bucket:

     def __init__(self):
          self.bucket_name = "cloud6-intern"

     def upload(self, file, object_name):
          s3 = session.resource('s3')
          try:
               s3.Bucket(self.bucket_name).upload_file(file, object_name)
               print('Success: File uploaded to S3')
          except FileNotFoundError:
               print('Error: File not found')

     def delete(self, object_name):
          s3 = session.resource('s3')
          try:
               s3.Object(self.bucket_name, object_name).delete()
               print('Success: File deleted')
          except FileNotFoundError:
               print('Error: File not found')
     
     def delete_fk(self, file_key):
          s3 = session.resource('s3')
          try:
               s3.Object(self.bucket_name, file_key).delete()
               print('Success: File deleted')
          except FileNotFoundError:
               print('Error: File not found')
     
     def object_exists(self, file_key):
          s3 = session.resource('s3')
          try:
               s3.Object(self.bucket_name, file_key).load()
               return True
          except FileNotFoundError:
               return False
     
     def download(self, object_name, file):
          s3 = session.resource('s3')
          try:
               s3.Bucket(self.bucket_name).download_file(object_name, file)
               print('Success: File downloaded')
          except FileNotFoundError:
               print('Error: File not found')

     def list(self):
          s3 = session.resource('s3')
          bucket = s3.Bucket(self.bucket_name)
          for obj in bucket.objects.all():
               print(obj.key)

     
               