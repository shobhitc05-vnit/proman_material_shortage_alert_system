import streamlit as st
import pandas as pd

# Load Excel file
df = pd.read_excel("inventory.xlsx")

# Filter critical materials
critical = df[df["Current_Stock"] < df["Safety_Stock"]]

# Dashboard title
st.title("Material Shortage Dashboard")

# KPI Card
st.metric(
    label="Materials Below Safety Stock",
    value=len(critical)
)

# Full inventory table
st.subheader("Current Inventory")
st.dataframe(df)

# Critical materials table
st.subheader("Critical Materials")
st.dataframe(critical)


st.bar_chart(
    df.set_index("Material_Name")["Current_Stock"]
)

