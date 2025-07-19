import streamlit as st
import pandas as pd
from src.clean import clean_data
from src.detect_anomalies import detect_outliers
from src.explain import explain_fix

st.set_page_config(page_title="AutoCleanAI", layout="wide")
st.title("🤖 AutoCleanAI - AI-Powered Data Cleaner")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Raw Data")
    st.write(df)

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if numeric_cols:
        df_anomaly = detect_outliers(df[numeric_cols], numeric_cols)
        df_anomaly['explanation'] = df_anomaly.apply(explain_fix, axis=1)

        st.subheader("⚠️ Anomalies Detected")
        st.write(df_anomaly[['anomaly', 'explanation'] + numeric_cols])

        cleaned_df = clean_data(df)
        st.subheader("✅ Cleaned Data")
        st.write(cleaned_df)

        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Cleaned Data", csv, "cleaned_data.csv", "text/csv")
