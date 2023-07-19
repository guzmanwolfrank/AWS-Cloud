import pandas as pd
import boto3

# Get the AWS CLI configuration
config = boto3.config.Config(region_name="us-east-1")

# Create a CSV file
csv_file_name = "my-data.csv"
with open(csv_file_name, "r") as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
        data.append(row)

# Create a pandas dataframe
df = pd.DataFrame(data)

# Create an S3 client
s3 = boto3.client("s3", config=config)

# Create a bucket
bucket_name = "my-bucket"
s3.create_bucket(Bucket=bucket_name)

# Upload the CSV file to the S3 bucket
s3.upload_file(Filename=csv_file_name, Bucket=bucket_name, Key=csv_file_name)
