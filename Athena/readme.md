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

## Project Description

This project aims to analyze healthcare data to gain insights into patient demographics, medical conditions, hospital admissions, billing, and medical test results. By leveraging AWS Glue to crawl and catalog the dataset, and using Amazon Athena for SQL-based analysis, we perform various queries to understand patterns and trends in the healthcare data.

## Goals

- Analyze patient demographics.
- Identify common medical conditions.
- Analyze hospital admissions and billing information.
- Identify trends in medical test results.

## SQL Queries

Write SQL queries to analyze the healthcare data using Amazon Athena. Sample queries could include:

- Total billing amount per hospital.
- Average age of patients by gender.
- Most common medical conditions.
- Length of hospital stay.
- Top medications prescribed.

## Data Dictionary

- **Name**: Patient's name.
- **Age**: Patient's age.
- **Gender**: Patient's gender.
- **Blood Type**: Patient's blood type.
- **Medical Condition**: Patient's medical condition.
- **Date of Admission**: Date of patient's admission to the hospital.
- **Doctor**: Attending doctor's name.
- **Hospital**: Name of the hospital.
- **Insurance Provider**: Patient's insurance provider.
- **Billing Amount**: Amount billed for the patient's treatment.
- **Room Number**: Patient's room number.
- **Admission Type**: Type of admission (e.g., inpatient, outpatient).
- **Discharge Date**: Date of patient's discharge from the hospital.
- **Medication**: Medication prescribed to the patient.
- **Test Results**: Results of medical tests conducted on the patient.

## Exploring the Data

Explore the dataset to understand its structure and contents before performing analysis. Use SQL queries to perform basic exploratory analysis.

## Findings

Document the findings from the analysis, including insights into patient demographics, medical conditions, hospital admissions, billing information, and medical test results.

## Conclusion

Summarize the key findings and insights gained from the analysis. Discuss potential implications and areas for further investigation.

## Tech Stack

- Amazon Athena
- AWS Glue
- Amazon S3



## License

This project is licensed under the [MIT License](LICENSE).
