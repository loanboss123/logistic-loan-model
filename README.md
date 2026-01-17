# Loan Approval Prediction – Logistic Regression

## Problem Statement
Build a production-ready machine learning pipeline to predict loan approval status
based on applicant demographic and financial features.

## Dataset
Kaggle Loan Approval Dataset.

## Approach
- Exploratory analysis and feature engineering in Jupyter
- Label encoding for categorical variables
- Outlier treatment and feature scaling
- Logistic Regression model
- Modular, reusable Python pipeline

## Project Structure
- notebooks/ → experimentation and EDA
- src/ → reusable production code
- main.py → single-command execution
- models/ → trained model artifacts

##Results
-Accuracy: ~92%
-Model evaluated using hold-out test set

## How to Run
```bash
conda env create -f environment.yml
conda activate loan_lr
python main.py

