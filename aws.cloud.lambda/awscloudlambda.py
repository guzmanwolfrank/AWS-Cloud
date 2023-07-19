import boto3
import json
import csv

# Get the AWS Lambda configuration
config = boto3.config.Config(region_name="us-east-1")

# Create a Lambda client
lambda_client = boto3.client("lambda", config=config)

# Get the Jupyter notebook file
notebook_file = "my-notebook.ipynb"
with open(notebook_file) as f:
     notebook_content = f.read()

# Convert the Jupyter notebook file to JSON
notebook_json = json.loads(notebook_content)

# Get the output of the Jupyter notebook file
output = notebook_json["cells"][0]["outputs"][0]["data"]["text/plain"]

# Create a CSV file
csv_file_name = "Datasheet.csv"
with open(csv_file_name, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([output])

# Invoke the Lambda function
lambda_client.invoke(FunctionName="my-lambda-function", Payload=json.dumps({"notebook_file": notebook_file}))
