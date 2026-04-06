# End-to-End Bank Marketing ML

## Project Overview

This project develops an end-to-end Machine Learning pipeline to predict whether a bank customer will subscribe to a term deposit based on marketing campaign data. The project covers the full Data Science workflow, including data analysis, preprocessing, feature engineering, model training, evaluation, and model selection.

The objective is to build classification models that help optimize marketing campaigns by identifying potential customers who are more likely to subscribe to a deposit product.

## Dataset

The dataset contains customer information, campaign details, and previous marketing interactions.

Target variable:
- deposit → Whether the customer subscribed to a term deposit (Yes/No)

## Main features include:
- Age
- Job
- Marital status
- Education
- Balance
- Housing loan
- Personal loan
- Contact type
- Campaign information
- Previous campaign outcome
- Project Workflow

## The project follows a complete Machine Learning pipeline:
- Data loading
- Exploratory Data Analysis (EDA)
- Data cleaning
- Feature engineering
- Train/Test split
- Data preprocessing using Pipeline and ColumnTransformer
- Model training
- Model comparison
- Feature importance analysis
- Model evaluation (Confusion Matrix, ROC Curve)
- Hyperparameter tuning (GridSearchCV)
- Ensemble model (Voting Classifier)
- Final model selection
- Model export
- Models Used

## The following Machine Learning models were trained and compared:
- Logistic Regression
- Random Forest
- Decision Tree
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Gradient Boosting
- Voting Classifier (Ensemble)

## Models were evaluated using:
- Accuracy
- Confusion Matrix
- ROC Curve
- AUC Score
- Feature Importance
- Training Time
- Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Plotly

## Project Structure
end-to-end-bank-marketing-ml/
│
├── data/
├── notebooks/
├── src/
├── model/
├── images/
├── README.md
├── requirements.txt
└── .gitignore

## Results

The project compares multiple classification models and selects the best performing model based on test accuracy and ROC-AUC score. Feature importance analysis helps identify the most relevant variables influencing customer subscription decisions.

# Author
Flavia Hepp
Machine Learning project focused on banking marketing campaign prediction and customer behavior analysis.
