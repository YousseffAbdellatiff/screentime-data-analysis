import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_excel('data.xlsx')

# Check for missing data and handle it (for simplicity, dropping rows with missing values here)
data = data.dropna()

# Convert categorical variables to numeric (Label Encoding)
label_encoder = LabelEncoder()

# For categorical columns like 'Gender' and 'Mental_Health_Status', apply LabelEncoder
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['Mental_Health_Status'] = label_encoder.fit_transform(data['Mental_Health_Status'])
data['Stress_Level'] = label_encoder.fit_transform(data['Stress_Level'])

# Select features (X) and target (y)
X = data[['Screen_Time_Hours', 'Stress_Level', 'Sleep_Hours', 'Physical_Activity_Hours', 'Age']]  # Features
y = data['Mental_Health_Status']  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predict on the test set
y_pred = rf.predict(X_test)

# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)

# Classification Report
classification_rep = classification_report(y_test, y_pred)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Streamlit Layout
st.set_page_config(page_title="Random Forest Model Results", page_icon="📊")

# Main Header
st.title("Random Forest Model for Mental Health Prediction")

# Display Model Accuracy as text
st.write(f"### Model Accuracy: {accuracy:.2f}")

# Display Classification Report as text
st.write("### Classification Report:")
st.text(classification_rep)

# Display Confusion Matrix as text
st.write("### Confusion Matrix:")
st.write(cm)

# Predict for a new instance (Example input)
st.write("### Predict for a New Instance")

# You can collect input for new predictions (just an example)
screen_time = st.number_input("Enter Screen Time Hours", min_value=0, max_value=24, value=5)
stress_level = st.selectbox("Select Stress Level", ["Low", "Medium", "High"])
sleep_hours = st.number_input("Enter Sleep Hours", min_value=0, max_value=24, value=8)
physical_activity = st.number_input("Enter Physical Activity Hours", min_value=0, max_value=24, value=2)
age = st.number_input("Enter Age", min_value=0, max_value=100, value=25)

# Encode the stress level input for prediction
stress_level_encoded = label_encoder.transform([stress_level])[0]

# Prepare the input data for prediction
new_data = pd.DataFrame({
    'Screen_Time_Hours': [screen_time],
    'Stress_Level': [stress_level_encoded],
    'Sleep_Hours': [sleep_hours],
    'Physical_Activity_Hours': [physical_activity],
    'Age': [age]
})

# Predict using the trained Random Forest model
prediction = rf.predict(new_data)

# Display the prediction result as text
predicted_status = 'Good' if prediction[0] == 1 else 'Bad' if prediction[0] == 0 else 'Fair'
st.write(f"Predicted Mental Health Status: {predicted_status}")
