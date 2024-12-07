import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Custom Visualization", page_icon="📊")

# Load the dataset
data = pd.read_excel('data.xlsx')

st.markdown("# Custom Visualization")
st.sidebar.header("Select Columns")

# Select columns for x and y
x_axis = st.sidebar.selectbox("Select X-Axis", options=data.columns)
y_axis = st.sidebar.selectbox("Select Y-Axis", options=data.columns)

if x_axis and y_axis:
    st.write(f"### {y_axis} vs {x_axis}")
    fig, ax = plt.subplots()
    ax.scatter(data[x_axis], data[y_axis], alpha=0.5)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    st.pyplot(fig)
else:
    st.warning("Please select both X and Y axes.")
