import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Stress and Usage Visualization", page_icon="📈")

# Load the dataset
data = pd.read_excel('data.xlsx')

st.markdown("# Stress and Usage Visualization")
st.sidebar.header("Visualization")

# Bar chart for stress levels
st.write("### Stress Levels")
stress_level_counts = data['Stress_Level'].value_counts()
st.bar_chart(stress_level_counts)

# Scatter plot of screen time vs. physical activity
st.write("### Screen Time vs Physical Activity")
scatter_chart = alt.Chart(data).mark_circle(size=60).encode(
    x='Screen_Time_Hours',
    y='Physical_Activity_Hours',
    color='Stress_Level',
    tooltip=['User_ID', 'Stress_Level']
)
st.altair_chart(scatter_chart, use_container_width=True)
