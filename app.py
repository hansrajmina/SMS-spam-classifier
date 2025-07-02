# spam_app.py
import streamlit as st
import pickle

# Load the trained pipeline
with open("spam_classifier.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📩 Spam Classifier Web App")

user_input = st.text_area("Enter a message to check if it's spam or not:")

if st.button("Predict"):
    result = model.predict([user_input])[0]
    st.write("🧾 **Prediction:**")
    st.success("✅ Not Spam" if result == 0 else "⚠️ Spam")
