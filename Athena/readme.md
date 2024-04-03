# Healthcare Data Analysis with Amazon Athena and AWS Glue

## Overview

This project demonstrates the process of analyzing healthcare data using Amazon Athena and AWS Glue. The dataset contains information about patients, including their demographic details, medical conditions, hospital admissions, billing information, and medical tests. By leveraging AWS Glue to crawl the dataset and create a table in the Glue Data Catalog, and using Amazon Athena for SQL-based analysis, we gain insights into the healthcare data.

## Dataset

The dataset provided is in CSV format and contains the following columns:

- Name
- Age
- Gender
- Blood Type
- Medical Condition
- Date of Admission
- Doctor
- Hospital
- Insurance Provider
- Billing Amount
- Room Number
- Admission Type
- Discharge Date
- Medication
- Test Results

Ensure the dataset is uploaded to an Amazon S3 bucket before setting up AWS Glue.

## AWS Glue Setup

1. Upload the dataset CSV file to an Amazon S3 bucket.
2. Set up an AWS Glue crawler to crawl the S3 bucket and create a table in the Glue Data Catalog. The crawler will infer the schema from the CSV file.

## Amazon Athena Queries

Write SQL queries to analyze the healthcare data using Amazon Athena. Sample queries could include:

- Total billing amount per hospital.
- Average age of patients by gender.
- Most common medical conditions.
- Length of hospital stay.
- Top medications prescribed.

## Documentation

Comprehensive documentation is provided to guide users through setting up and executing the project. Documentation covers:

- Setup instructions for AWS Glue and Amazon Athena
- Execution of AWS Glue crawler
- Running queries in Amazon Athena
- Interpreting analysis results

Refer to the documentation in the `docs/` directory for detailed instructions.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine:

