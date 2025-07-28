import pandas as pd
import matplotlib as plt
import streamlit as st

st.title("📊 Automated Sales Report Generator")

uploaded_file = st.file_uploader("Upload CSV or Excel File", type=['csv', 'xlsx'])

if uploaded_file:
    try:
        # Read file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        df['Revenue'] = df['Units Sold'] * df['Unit Price']
        summary = df.groupby('Product')['Revenue'].sum()
        total_revenue = summary.sum()
        top_product = summary.idxmax()

        st.subheader("📌 Sales Summary")
        for product, revenue in summary.items():
            st.write(f"**{product}** – Revenue: {int(revenue)} PKR")

        st.success(f"💰 Total Revenue: {int(total_revenue)} PKR")
        st.info(f"🏆 Top Product: **{top_product}**")

        # Bar chart
        st.subheader("📈 Revenue by Product")
        st.bar_chart(summary)

    except Exception as e:
        st.error(f"Error: {e}")
