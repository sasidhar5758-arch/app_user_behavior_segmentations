import streamlit as st
import pandas as pd

st.title("📊 App User Behavior Segmentation")

df = pd.read_csv(
    "data/processed/clustered_data.csv"
)

st.subheader("Cluster Distribution")

st.bar_chart(
    df["Cluster"].value_counts()
)

st.subheader("Sample Data")

st.dataframe(df.head())