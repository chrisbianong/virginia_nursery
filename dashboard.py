import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Title and description
st.title("Virginia Nursery Forecasting Dashboard")
st.write("AI-powered insights to optimize inventory and meet customer demand.")

# Sidebar for user inputs
st.sidebar.header("Input Parameters")
inventory = st.sidebar.slider("Current Inventory (Units)", 0, 100, 50)
sales_trend = st.sidebar.selectbox("Sales Trend", ["Increasing", "Stable", "Decreasing"])
weather = st.sidebar.selectbox("Weather Conditions", ["Hot", "Mild", "Cold"])

# AI Forecast Simulation
forecast_multiplier = {"Increasing": 1.3, "Stable": 1.0, "Decreasing": 0.7}[sales_trend]
weather_impact = {"Hot": 1.2, "Mild": 1.0, "Cold": 0.8}[weather]
forecasted_sales = int(inventory * forecast_multiplier * weather_impact)

# Display metrics
st.metric("Forecasted Sales (Next Month)", forecasted_sales)
restocking_recommendation = max(0, 100 - inventory)
st.metric("Recommended Restocking", restocking_recommendation)

# Visualization of historical sales
st.header("Historical Sales Data")
data = pd.DataFrame({
    "Month": ["January", "February", "March", "April", "May"],
    "Sales": [200, 220, 250, 240, 270]
})
st.line_chart(data.set_index("Month"))

# File uploader for inventory data
st.sidebar.header("Upload Your Inventory Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Inventory Data:")
    st.write(data)


# Plotly visualization for sales data
fig = px.bar(data, x="Month", y="Sales", title="Monthly Sales")
st.plotly_chart(fig)
