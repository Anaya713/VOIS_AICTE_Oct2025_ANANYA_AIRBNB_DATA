
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Airbnb Data Analytics", layout="wide")
st.title("Airbnb Data Analytics Dashboard 🏠")

# File upload
st.sidebar.header("Upload Your Airbnb Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data Loaded Successfully! ✅")
    
    # Show raw data
    if st.checkbox("Show Raw Data"):
        st.dataframe(df.head(10))
    
    st.header("Pricing Analysis 💰")
    if 'price' in df.columns:
        # Clean price column if needed
        df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
        fig, ax = plt.subplots()
        sns.histplot(df['price'], bins=50, kde=True, color='skyblue', ax=ax)
        ax.set_title("Price Distribution")
        st.pyplot(fig)
    else:
        st.warning("No 'price' column found in dataset!")

    st.header("Availability Analysis 📅")
    if 'availability_365' in df.columns:
        fig2, ax2 = plt.subplots()
        sns.histplot(df['availability_365'], bins=50, kde=False, color='orange', ax=ax2)
        ax2.set_title("Availability Distribution (Days per Year)")
        st.pyplot(fig2)
    else:
        st.warning("No 'availability_365' column found in dataset!")

    st.header("Top 10 Neighborhoods 🏘️")
    if 'neighbourhood' in df.columns:
        top_neigh = df['neighbourhood'].value_counts().head(10)
        fig3, ax3 = plt.subplots()
        sns.barplot(x=top_neigh.values, y=top_neigh.index, palette="viridis", ax=ax3)
        ax3.set_title("Top 10 Neighborhoods by Listings")
        st.pyplot(fig3)
    else:
        st.warning("No 'neighbourhood' column found in dataset!")

else:
    st.info("Please upload a CSV file to get started.")
