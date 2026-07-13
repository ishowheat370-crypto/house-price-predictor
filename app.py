import streamlit as st
import pandas as pd

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ---------------------------------
# Title
# ---------------------------------
st.title("🏠 House Price Predictor")
st.write("Enter the house details below to predict its price.")

st.divider()

# ---------------------------------
# Sidebar
# ---------------------------------
st.sidebar.header("House Details")

area = st.sidebar.number_input(
    "Area (sq ft)",
    min_value=100,
    max_value=10000,
    value=1500
)

bedrooms = st.sidebar.slider(
    "Bedrooms",
    1,
    10,
    3
)

bathrooms = st.sidebar.slider(
    "Bathrooms",
    1,
    10,
    2
)

stories = st.sidebar.slider(
    "Stories",
    1,
    5,
    2
)

parking = st.sidebar.slider(
    "Parking Spaces",
    0,
    5,
    1
)

mainroad = st.sidebar.selectbox(
    "Main Road",
    ["Yes", "No"]
)

guestroom = st.sidebar.selectbox(
    "Guest Room",
    ["Yes", "No"]
)

basement = st.sidebar.selectbox(
    "Basement",
    ["Yes", "No"]
)

hotwater = st.sidebar.selectbox(
    "Hot Water Heating",
    ["Yes", "No"]
)

airconditioning = st.sidebar.selectbox(
    "Air Conditioning",
    ["Yes", "No"]
)

# ---------------------------------
# Convert Yes/No to 1/0
# ---------------------------------
yes_no = {
    "Yes": 1,
    "No": 0
}

data = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "parking": [parking],
    "mainroad": [yes_no[mainroad]],
    "guestroom": [yes_no[guestroom]],
    "basement": [yes_no[basement]],
    "hotwaterheating": [yes_no[hotwater]],
    "airconditioning": [yes_no[airconditioning]]
})

# ---------------------------------
# Show Input
# ---------------------------------
st.subheader("Input Features")
st.dataframe(data, use_container_width=True)

# ---------------------------------
# Predict Button
# ---------------------------------
if st.button("Predict House Price"):

    # Replace this section with your Orange model prediction
    # Example:
    #
    # prediction = model(data)
    #
    # OR
    #
    # prediction = model.predict(data)
    #
    # depending on your exported model.

    prediction = "Model Not Loaded"

    st.success(f"Predicted Price: {prediction}")

st.divider()
st.caption("Built with Streamlit • Orange Data Mining • Machine Learning")
