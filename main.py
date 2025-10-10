import streamlit as st
import pandas as pd
import joblib

# Load model and columns
lr = joblib.load("house_price_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("HOUSE PRICE PREDICTION")

# Select house type
l = st.selectbox("What type of housing you want", ["HOUSE", "FLAT", "APARTMENTMENT"])

# Inputs (always visible)
st.write(f"So your {l} should have")

area = st.number_input("Enter the area of house you want in sq.feet", min_value=500, max_value=100000, step=500)
bedroom = st.slider("How many bedrooms you wish to have in your house", 1, 5, 2)
bathroom = st.slider("How many bathrooms you wish to have in your house", 1, 5, 2)
stories = st.slider("How many floors you wish to have", 1, 4, 1)
parking = st.slider("How many parking spaces you want", 0, 5, 1)

road = st.radio("Do you wish to buy a house at the main road", ["YES", "NO"])
guest = st.radio("Do you wish to have a guest room in your house", ["YES", "NO"])
base = st.radio("Do you wish to have a basement", ["YES", "NO"])
hot = st.radio("Do you wish that your house should have an inbuilt geyser", ["YES", "NO"])
ac = st.radio("Do you wish that your house should have an inbuilt air conditioner", ["YES", "NO"])
pref = st.radio("Do you need prefarea", ["YES", "NO"])
fur = st.radio("Do you wanna buy a house which is", ["FURNISHED", "SEMI FURNISHED", "UNFURNISHED"])

# Prepare user data
user_data = {
    'area': area,
    'bedrooms': bedroom,
    'bathrooms': bathroom,
    'stories': stories,
    'parking': parking,
    'mainroad_yes': 1 if road == "YES" else 0,
    'mainroad_no': 1 if road == "NO" else 0,
    'guestroom_yes': 1 if guest == "YES" else 0,
    'guestroom_no': 1 if guest == "NO" else 0,
    'basement_yes': 1 if base == "YES" else 0,
    'basement_no': 1 if base == "NO" else 0,
    'hotwaterheating_yes': 1 if hot == "YES" else 0,
    'hotwaterheating_no': 1 if hot == "NO" else 0,
    'airconditioning_yes': 1 if ac == "YES" else 0,
    'airconditioning_no': 1 if ac == "NO" else 0,
    'prefarea_yes': 1 if pref == "YES" else 0,
    'prefarea_no': 1 if pref == "NO" else 0,
    'furnishingstatus_furnished': 1 if fur == "FURNISHED" else 0,
    'furnishingstatus_semi-furnished': 1 if fur == "SEMI FURNISHED" else 0,
    'furnishingstatus_unfurnished': 1 if fur == "UNFURNISHED" else 0
}

# Convert to DataFrame and align columns
new_house = pd.DataFrame([user_data])
new_house = new_house.reindex(columns=model_columns, fill_value=0)

# ✅ Predict button (independent, not inside any "if l:")
if st.button("💰 Predict House Price"):
    predicted_price = lr.predict(new_house)[0]
    st.success(f"Predicted Price: ₹{predicted_price:,.2f}")
    st.info(f"≈ {predicted_price/1e5:.2f} lakhs or {predicted_price/1e7:.2f} crores")
