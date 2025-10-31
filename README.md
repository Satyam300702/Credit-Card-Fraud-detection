# 💳 Credit Card Fraud Detection using Stacking Ensemble

# 🚀 Overview
This project detects fraudulent credit card transactions using a stacking ensemble model that combines XGBoost, LightGBM, and Logistic Regression.
The dataset is highly imbalanced, so SMOTE (Synthetic Minority Over-sampling Technique) is applied to balance the data before training.
------------------------------------------------------------------------------------------------------------------------------------------------
📊 Dataset

Source: Credit Card Fraud Detection Dataset (Kaggle)

Rows: 284,807

Columns: 31

Target Variable: Class →

0: Non-Fraud

1: Fraud
------------------------------------------------------------------------------------------------------------------------------------------------

# ⚙️ Features Used

Numerical Features: V1, V2, …, V28 (Anonymized PCA components)

Amount: Transaction amount (scaled using StandardScaler)

Removed: Time (not relevant for fraud prediction)

------------------------------------------------------------------------------------------------------------------------------------------------

# 🧾 Model Performance
Metric	Score
Accuracy	0.9991
ROC-AUC	0.9447
CV ROC-AUC	0.9786
------------------------------------------------------------------------------------------------------------------------------------------------
# Key Learnings

Handling class imbalance using SMOTE

Building Stacking Ensemble models

Using RandomizedSearchCV for hyperparameter tuning

Evaluating models using ROC-AUC, Confusion Matrix, and Cross-Validation
------------------------------------------------------------------------------------------------------------------------------------------------
👨‍💻 Author

Satyam Kumar
2nd Year CSE (AI & ML) Student

GitHub:- https://github.com/Satyam300702
Linkedlin :- www.linkedin.com/in/satyam-kumar-558269328