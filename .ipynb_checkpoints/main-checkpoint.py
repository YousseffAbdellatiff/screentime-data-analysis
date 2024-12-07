import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Dashboard", page_icon="📊")

# Load the dataset
data = pd.read_excel('data.xlsx')

# Main Page
st.markdown("# Data Dashboard")
st.sidebar.header("Navigation")

st.write("### Overview of Data")
st.write(data.head())  # Show the first few rows of the data

st.write("### Summary Statistics")
st.write(data.describe().transpose())  # Show basic statistics for numeric columns

# Visualizing a bar chart for numeric columns
st.write("### Data Visualization")
numeric_columns = data.select_dtypes(include='number')
if not numeric_columns.empty:
    st.bar_chart(numeric_columns)
else:
    st.warning("No numeric columns to visualize.")

# Scatter plot of screen time and physical activity
st.write("In the following graph, We will show the relation between the screen time hours and physical activity hours")
sns.scatterplot(data=data, x="Screen_Time_Hours", y="Physical_Activity_Hours", color="blue")
st.pyplot(plt)

# Display correlation between screen time and sleep hours
correlation = data["Screen_Time_Hours"].corr(data["Sleep_Hours"])
st.write(f"Correlation between Screen Time Hours and Sleep Hours: {correlation}")

# Now, show the relationship between 'Mental_Health_Status' and 'Screen_Time_Hours'
st.write("### Relationship between Mental Health Status and Screen Time Hours")

# Boxplot for screen time hours by mental health status
sns.boxplot(x="Mental_Health_Status", y="Screen_Time_Hours", data=data)
plt.title("Screen Time Hours by Mental Health Status")
plt.xlabel("Mental Health Status")
plt.ylabel("Screen Time Hours")
st.pyplot(plt)

# Alternatively, a violin plot to show distribution
st.write("### Distribution of Screen Time Hours by Mental Health Status (Violin Plot)")
sns.violinplot(x="Mental_Health_Status", y="Screen_Time_Hours", data=data, inner="quart")
plt.title("Distribution of Screen Time Hours by Mental Health Status")
plt.xlabel("Mental Health Status")
plt.ylabel("Screen Time Hours")
st.pyplot(plt)

# Barplot to show average screen time hours for each mental health status
st.write("### Average Screen Time Hours by Mental Health Status")
mean_screen_time = data.groupby('Mental_Health_Status')['Screen_Time_Hours'].mean().reset_index()
sns.barplot(x='Mental_Health_Status', y='Screen_Time_Hours', data=mean_screen_time)
plt.title("Average Screen Time Hours by Mental Health Status")
plt.xlabel("Mental Health Status")
plt.ylabel("Average Screen Time Hours")
st.pyplot(plt)

