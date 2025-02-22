# Banking Churn Prediction Using AWS Sagemaker
* Banking churn prediction using AWS SageMaker

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Steps](#steps)
4. [Environment Setup](#environment-setup)
5. [Kaggle setup](#kaggle-setup)
6. [AWS CLI](#aws-cli)


## Project Overview
* The project is about predicting the churn of bank customers using AWS SageMaker. 
* The dataset used in this project is from Kaggle. 
* The dataset contains information about bank customers and their churn status, which indicates whether they have exited the bank or not.

## Dataset
* The dataset contains 10,000 records and 14 columns.
* The columns are as follows:
  * RowNumber: The sequential number assigned to each row in the dataset.
  * CustomerId: A unique identifier for each customer.
  * Surname: The surname of the customer.
  * CreditScore: The credit score of the customer.
  * Geography: The geographical location of the customer (e.g., country or region).
  * Gender: The gender of the customer.
  * Age: The age of the customer.
  * Tenure: The number of years the customer has been with the bank.
  * Balance: The account balance of the customer.
  * NumOfProducts: The number of bank products the customer has.
  * HasCrCard: Indicates whether the customer has a credit card (binary: yes/no).
  * IsActiveMember: Indicates whether the customer is an active member (binary: yes/no).
  * EstimatedSalary: The estimated salary of the customer.
  * Exited: Indicates whether the customer has exited the bank (binary: yes/no).
* The target variable is `Exited`, which indicates whether the customer has exited the bank or not.

## Steps
1. Create a `conda` environment and install the required packages.
2. Get the data from Kaggle.

## Environment Setup
* Create `conda` environment
```bash
conda create -n sagemaker python=3.10
conda activate sagemaker
```
* Install required packages
```bash
pip install -r requirements.txt
```
* Deactivate the environment
```bash
conda deactivate
```

## Kaggle setup
* Create a Kaggle account and get the API key.
* Create a directory called `.kaggle` in the home directory.
* Create a file called `kaggle.json` in the `.kaggle` directory.
* Add the following content to the `kaggle.json` file:
```json
{
  "username": "your-kaggle-username",
  "key": "your-kaggle-api-key"
}
```
* Change the permissions of the `kaggle.json` file:
```bash
chmod 600 ~/.kaggle/kaggle.json
```
* Install the Kaggle package or add this to the `requirements.txt` file:
```bash
pip install kaggle
```

## AWS CLI
* Install and configure `awscli`
* Give the userdetails, access key and secret access key

## Project Steps
* Get the data into the `data/raw` folder
* Read the data into dataframes
* Perform the EDA 
* Split the data into train and test sets
* Save them as csv files in `data/processed`
* Use column transformer to transform the data
* Save the column transformer as a pickle object
* We can use the saved pre-processing pickle object for the below purposes
  * Data Transformation for New Data: 
    * Whenever you get new data that needs to be transformed in the same way as your training data, you can use the saved column transformer. This ensures consistency in data processing.
  * Model Deployment: 
    * When deploying your model in a production environment, you'll need the same column transformer to preprocess incoming data before making predictions. This is crucial to maintain the accuracy of your model.
  * Cross-Validation and Testing: 
    * If you perform cross-validation or test your model on different subsets of data, you'll need to apply the same transformations to ensure that the data is treated consistently.
  * Reproducibility:
    * In research or iterative development, using the saved transformer allows you to replicate your experiments accurately. 
    * This is essential for verifying your results and maintaining the integrity of your work.
