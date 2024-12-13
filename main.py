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
st.write("In the following graph, We will show the relation between the screen time hours and Sleep hours")
sns.scatterplot(data=data, x="Screen_Time_Hours", y="Sleep_Hours", color="blue")
st.pyplot(plt)

# Display correlation between screen time and sleep hours
correlation = data["Screen_Time_Hours"].corr(data["Sleep_Hours"])
st.write(f"Correlation between Screen Time Hours and Sleep Hours: {correlation}")
\







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

# Function to generate fake data
def generate_fake_data(num_samples):
    fake_data = []
    for _ in range(num_samples):
        fake_data.append({
            "User_ID": f"FAKE-{str(np.random.randint(10000, 99999))}",
            "Age": np.random.randint(18, 60),  # Assume ages between 18 and 60
            "Gender": np.random.choice(["Male", "Female"], p=[0.5, 0.5]),
            "Technology_Usage_Hours": round(np.random.uniform(1, 10), 2),
            "Social_Media_Usage_Hours": round(np.random.uniform(0.5, 8), 2),
            "Gaming_Hours": round(np.random.uniform(0, 5), 2),
            "Screen_Time_Hours": round(np.random.uniform(4, 15), 2),
            "Mental_Health_Status": np.random.choice(["Excellent", "Good", "Fair", "Poor"]),
            "Stress_Level": np.random.choice(["Low", "Medium", "High"], p=[0.4, 0.4, 0.2]),
            "Sleep_Hours": round(np.random.uniform(4, 10), 2),
            "Physical_Activity_Hours": round(np.random.uniform(0, 10), 2),
            "Support_Systems_Access": np.random.choice(["Yes", "No"], p=[0.6, 0.4]),
            "Work_Environment_Impact": np.random.choice(["Positive", "Negative"]),
            "Online_Support_Usage": np.random.choice(["Yes", "No"], p=[0.3, 0.7]),
        })
    return pd.DataFrame(fake_data)
    
# Number of fake samples (25-50% of 1500)
num_fake_samples = np.random.randint(375, 750)

# Generate fake data
fake_data_df = generate_fake_data(num_fake_samples)

# Combine original and fake data
combined_data = pd.concat([original_data, fake_data_df], ignore_index=True)

# Save to a new file
combined_data.to_csv("combined_data.csv", index=False)

print(f"Generated {num_fake_samples} fake records and combined them with the original dataset!")