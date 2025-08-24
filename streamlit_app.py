import streamlit as st
import pandas as pd
import joblib

# -----------------------------
#  Model
# -----------------------------
model = joblib.load("final_model_churn.joblib")

def get_prediction(data: pd.DataFrame):
    pred = model.predict(data)
    pred_proba = model.predict_proba(data)
    return pred, pred_proba

# -----------------------------
# Page
# -----------------------------
st.set_page_config(
    page_title="EC Bank - Customer Churn Prediction",
    layout="centered",
)

# -----------------------------
# Title
# -----------------------------
st.subheader("EuroCyan Bank")
st.markdown("Customer Churn Prediction System")
st.markdown("---")
st.title("Customer Churn Prediction")
st.markdown("""
This app predicts if a customer will leave the bank based on their profile and account activity.
""")


# -----------------------------
# Background, Text Color
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #223c60;
        color: #f5f3e7
    }""", unsafe_allow_html=True)


# -----------------------------
# Customer Input
# -----------------------------
st.header("Enter Customer Details")

surname = st.text_input("Surname")
credit_score = st.number_input("Credit Score", min_value=0, max_value=1000, value=500)
geography = st.selectbox("Geography", ["Germany", "France", "Spain"])
gender = st.selectbox("Gender", ["Female", "Male"])
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.selectbox("Tenure (years with bank)", [0,1,2,3,4,5,6,7,8,9,10])
balance = st.number_input("Account Balance (EUR)", min_value=0, max_value=300000, value=1000)
num_of_products = st.selectbox("Number of Products", [1,2,3,4])
has_cr_card = st.selectbox("Has Credit Card?", ["No", "Yes"])
is_active_member = st.selectbox("Active Member?", ["No", "Yes"])
estimated_salary = st.number_input("Estimated Salary (EUR)", min_value=0, max_value=250000, value=50000)

# -----------------------------
# Hasil Input
# -----------------------------
st.header("Customer Profile Summary")
st.write(f"**Surname:** {surname}")
st.write(f"**Credit Score:** {credit_score}")
st.write(f"**Geography:** {geography}")
st.write(f"**Gender:** {gender}")
st.write(f"**Age:** {age}")
st.write(f"**Tenure:** {tenure} years")
st.write(f"**Balance:** {balance} EUR")
st.write(f"**Number of Products:** {num_of_products}")
st.write(f"**Has Credit Card:** {has_cr_card}")
st.write(f"**Active Member:** {is_active_member}")
st.write(f"**Estimated Salary:** {estimated_salary} EUR")

# -----------------------------
# Dataframe
# -----------------------------
data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Geography": [geography],
    "Gender": [gender],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_of_products],
    "HasCrCard": [1 if has_cr_card=="Yes" else 0],
    "IsActiveMember": [1 if is_active_member=="Yes" else 0],
    "EstimatedSalary": [estimated_salary]
})


# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict Churn"):
    pred, pred_proba = get_prediction(data)
    
    threshold = 0.5
    churn_prob = pred_proba[0][1]  # probability of churn
    churn_label = "Churn" if churn_prob > threshold else "Stay"

    st.subheader("Prediction Result")
    st.write(f"**Customer:** Mr/Mrs {surname}")
    st.write(f"**Churn Prediction:** {churn_label}")
    st.write(f"**Probability of Churn:** {churn_prob*100:.2f}%")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:12px;'>"
    "EC Bank - Customer Churn Prediction System | Built with Streamlit | © 2025 Istyarahma Kusumastuti"
    "</p>",
    unsafe_allow_html=True
)