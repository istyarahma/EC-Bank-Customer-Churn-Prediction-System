# Bank Customer Churn Prediction System  

A machine learning project to predict **bank customer churn** and help identify at-risk customers.  
This project was built as part of a Data Science bootcamp and deployed using **Streamlit**.  

---

## Project Overview  
Customer churn is when a customer stops using a company’s product or service.  
In banking, churn means customers closing their accounts or no longer being active.  
This project aims to build a prediction model so that the bank can take proactive actions to retain customers.  

---

## Dataset  
The dataset contains customer information such as:  

- **Demographic Features**: Geography, Gender, Age, Surname  
- **Behavioral Features**: Tenure, NumOfProducts, HasCrCard, IsActiveMember  
- **Financial Features**: CreditScore, Balance, EstimatedSalary

Target variable: **Exited (0 = Stay, 1 = Churn)**  

---

## Methodology  
1. **Data Preprocessing**: Handling missing values, encoding categorical features, feature scaling.  
2. **Exploratory Data Analysis (EDA)**: Understanding churn patterns (e.g., customers with low balance or short tenure are more likely to churn).  
3. **Modeling**: Compared Logistic Regression, Random Forest, AdaBoost, etc.  
4. **Evaluation**: Used F2-score and accuracy to select the best model.  
5. **Deployment**: Deployed the best-performing model on **Streamlit** for real-time prediction.  

---

## 🚀 Streamlit App  
The app allows users to:  
- Input customer details (e.g., Age, Balance, Tenure, etc.).  
- Get **churn prediction result** (Yes/No + probability score).   

Run locally:  
```bash
streamlit run app.py
