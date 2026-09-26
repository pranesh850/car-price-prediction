import streamlit as st
import joblib
import pandas as pd

# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = joblib.load("car_price_model.pkl")


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #777777;
    margin-bottom: 30px;
}

.price-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    background-color: #e8f1ff;
    color: #1f2937;
    margin-top: 20px;
    border: 1px solid #c7dcff;
}

.price {
    font-size: 36px;
    font-weight: 700;
    color: #1f2937;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🚗 Car Price Predictor")

    st.markdown("---")

    st.subheader("📌 About the Project")

    st.write(
        "This Machine Learning project predicts the estimated "
        "selling price of a used car based on its details."
    )

    st.markdown("---")

    st.subheader("🤖 Model Information")

    st.write("**Algorithm:** Random Forest Regressor")
    st.write("**Number of Features:** 7")
    st.write("**Dataset Size:** 30 records")
    st.write("**R² Score:** 0.80")

    st.markdown("---")

    st.subheader("📊 Features Used")

    st.write("• Manufacturing Year")
    st.write("• Present Price")
    st.write("• Kilometers Driven")
    st.write("• Previous Owners")
    st.write("• Fuel Type")
    st.write("• Seller Type")
    st.write("• Transmission")

    st.markdown("---")

    st.info(
        "Note: This project uses a small dataset of 30 records. "
        "Predictions are intended for demonstration purposes."
    )


# --------------------------------------------------
# Main Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🚗 Car Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict the estimated selling price '
    'of a used car using Machine Learning.</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Input Section
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("🚘 Car Information")

    year = st.number_input(
        "Manufacturing Year",
        min_value=2000,
        max_value=2026,
        value=2017
    )

    present_price = st.number_input(
        "Current Market Price (₹ lakhs)",
        min_value=0.0,
        value=10.0,
        step=0.1
    )

    kms_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        value=20000,
        step=1000
    )

    owner = st.number_input(
        "Previous Owners",
        min_value=0,
        max_value=3,
        value=0
    )


with col2:

    st.subheader("⚙️ Vehicle Details")

    fuel_type = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel"]
    )

    seller_type = st.selectbox(
        "Seller Type",
        ["Dealer", "Individual"]
    )

    transmission = st.selectbox(
        "Transmission",
        ["Manual", "Automatic"]
    )


# --------------------------------------------------
# Prediction Button
# --------------------------------------------------

st.markdown("---")

predict_button = st.button(
    "🔮 Predict Selling Price",
    use_container_width=True
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if predict_button:

    fuel_petrol = 1 if fuel_type == "Petrol" else 0

    seller_individual = (
        1 if seller_type == "Individual" else 0
    )

    transmission_manual = (
        1 if transmission == "Manual" else 0
    )


    new_car = pd.DataFrame({
        "Year": [year],
        "Present_Price": [present_price],
        "Kms_Driven": [kms_driven],
        "Owner": [owner],
        "Fuel_Type_Petrol": [fuel_petrol],
        "Seller_Type_Individual": [seller_individual],
        "Transmission_Manual": [transmission_manual]
    })


    predicted_price = model.predict(new_car)[0]


    # --------------------------------------------------
    # Prediction Result
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("💰 Prediction Result")

    st.markdown(
        f'<div class="price-box">'
        f'<div>Estimated Selling Price</div>'
        f'<div class="price">₹ {predicted_price:.2f} Lakhs</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.success("Prediction completed successfully!")


    # --------------------------------------------------
    # Price Comparison
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("📊 Price Comparison")

    comparison_data = pd.DataFrame(
        {
            "Price (₹ Lakhs)": [
                present_price,
                predicted_price
            ]
        },
        index=[
            "Current Market Price",
            "Predicted Selling Price"
        ]
    )

    st.bar_chart(comparison_data)


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Built with Python • Pandas • Scikit-learn • "
    "Random Forest • Streamlit"
)