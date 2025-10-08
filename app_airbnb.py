
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Airbnb Data Analytics", layout="wide")

st.title("Airbnb Data Analytics Dashboard")

uploaded_file = st.file_uploader("Upload your Airbnb CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    
    if st.checkbox("Show raw data"):
        st.dataframe(df.head())

    st.subheader("Dataset Info")
    buffer = []
    df.info(buf=buffer)
    s = '\n'.join(buffer)
    st.text(s)
    
    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

    st.subheader("Visualizations")

    if 'price' in df.columns:
        st.markdown("**Price Distribution**")
        fig, ax = plt.subplots()
        sns.histplot(df['price'], bins=50, kde=True, ax=ax)
        st.pyplot(fig)

    if 'room_type' in df.columns:
        st.markdown("**Room Type Count**")
        fig, ax = plt.subplots()
        sns.countplot(x='room_type', data=df, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    if 'neighbourhood_group' in df.columns:
        st.markdown("**Neighbourhood Group Count**")
        fig, ax = plt.subplots()
        sns.countplot(x='neighbourhood_group', data=df, ax=ax)
        st.pyplot(fig)

    st.markdown("**Correlation Heatmap**")
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 1:
        fig, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
else:
    st.info("Please upload a CSV file to start the analysis.")
