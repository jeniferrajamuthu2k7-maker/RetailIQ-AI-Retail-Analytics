import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# -------------------------
# PAGE CONFIGURATION
# -------------------------

st.set_page_config(
    page_title="RetailIQ AI",
    page_icon="🛒",
    layout="wide"
)
# -------------------------
# LOAD MODEL
# -------------------------

model = joblib.load("retail_sales_model.pkl")

# -------------------------
# LOAD DATASET
# -------------------------

df = pd.read_csv("Retailstores_Cleaned.csv")

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

h1{
    color:#0F172A;
    font-weight:700;
}

h2,h3{
    color:#1E3A8A;
}

div[data-testid="stMetric"]{
    background:#FFFFFF;
    padding:18px;
    border-radius:12px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.08);
    border-left:6px solid #2563EB;
}

.stButton>button{
    background:#2563EB;
    color:white;
    border-radius:10px;
    height:55px;
    width:100%;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1D4ED8;
}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.image(
    "https://img.icons8.com/color/240/shop.png",
    width=120
)

st.sidebar.title("RetailIQ AI")

st.sidebar.markdown("---")

st.sidebar.success("AI Powered Retail Analytics")

st.sidebar.markdown("## 📌 Project")

st.sidebar.write("Retail Revenue Prediction")

st.sidebar.markdown("## 🤖 Machine Learning")

st.sidebar.write("Random Forest Regressor")

st.sidebar.markdown("## 📈 Accuracy")

st.sidebar.success("99.97%")

st.sidebar.markdown("## 👩‍💻 Developer")

st.sidebar.write("Jenifer R")

st.sidebar.markdown("---")

st.sidebar.info(
"""
Technologies Used

• Python

• Pandas

• Streamlit

• Scikit-learn

• Power BI

• GitHub
"""
)

# -------------------------
# HERO SECTION
# -------------------------

left,right=st.columns([4,1])

with left:

    st.title("🛒 RetailIQ AI")

    st.subheader("Smart Retail Revenue Prediction")

    st.write(
        """
Predict retail revenue instantly using Machine Learning.

This AI application helps retailers estimate expected revenue
based on product, category and pricing information.
"""
    )

with right:

    st.image(
        "https://img.icons8.com/fluency/240/shopping-cart-loaded.png",
        width=150
    )

st.markdown("---")

# -------------------------
# KPI CARDS
# -------------------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("Products",len(df))

with c2:
    st.metric("Categories",df["Category"].nunique())

with c3:
    st.metric("Brands",df["Brand"].nunique())

with c4:
    st.metric("Model Accuracy","99.97%")

st.markdown("---")
# ======================================
# PRODUCT DETAILS
# ======================================

st.header("📝 Product Details")

# Dropdown Dictionaries

categories = {
    "Grocery":0,
    "Household":1,
    "Snacks":2,
    "Personal Care":3,
    "Dairy":4,
    "Unknown":5,
    "Beverages":6
}

brands = {
    "Aashirvaad":0,
    "Surf Excel":1,
    "Lays":2,
    "Lux":3,
    "Fortune":4,
    "Aavin":5,
    "Tata Tea":6,
    "Madhur":7,
    "Unknown":8,
    "Cadbury":9,
    "Britannia":10
}

payment_modes = {
    "CASH":0,
    "UPI":1,
    "CARD":2
}

months = {
    "January":0,
    "February":1,
    "March":2,
    "April":3,
    "May":4,
    "June":5
}

left,right = st.columns(2)

with left:

    category = st.selectbox(
        "📦 Select Category",
        list(categories.keys())
    )

    brand = st.selectbox(
        "🏷️ Select Brand",
        list(brands.keys())
    )

    payment = st.selectbox(
        "💳 Payment Mode",
        list(payment_modes.keys())
    )

    month = st.selectbox(
        "📅 Month",
        list(months.keys())
    )

with right:

    quantity = st.number_input(
        "📦 Quantity",
        min_value=1,
        value=1
    )

    selling_price = st.number_input(
        "💰 Selling Price (₹)",
        min_value=1,
        value=100
    )

    cost_price = st.number_input(
        "💸 Cost Price (₹)",
        min_value=1,
        value=80
    )

st.markdown("")

# ======================================
# PREDICT BUTTON
# ======================================

if st.button("🚀 Predict Revenue"):

    input_data = [[

        categories[category],

        brands[brand],

        quantity,

        selling_price,

        cost_price,

        payment_modes[payment],

        months[month]

    ]]

    prediction = model.predict(input_data)

    st.markdown("---")

    st.success(
        f"💰 Predicted Revenue : ₹ {prediction[0]:,.2f}"
    )
    st.info("✅ Prediction generated successfully using the trained Random Forest Regression model.")
    # ======================================
# AI INSIGHTS
# ======================================

st.markdown("---")

profit = max(0, prediction[0] - (quantity * cost_price))

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="💵 Predicted Revenue",
        value=f"₹ {prediction[0]:,.2f}"
    )

with col2:
    st.metric(
        label="📈 Estimated Profit",
        value=f"₹ {profit:,.2f}"
    )

st.markdown("---")

st.subheader("🤖 AI Business Recommendation")

# Recommendation based on predicted revenue

if prediction[0] >= 1000:

    st.success("""
### 🔥 High Revenue Expected

✅ Increase inventory

✅ Maintain product availability

✅ Promote premium products

✅ Good sales opportunity
""")

elif prediction[0] >= 500:

    st.warning("""
### 📦 Moderate Revenue Expected

• Keep regular stock

• Offer bundle discounts

• Monitor weekly sales
""")

else:

    st.error("""
### ⚠ Low Revenue Expected

• Consider promotional offers

• Improve product visibility

• Review pricing strategy

• Increase marketing
""")

st.markdown("---")

st.subheader("📋 Prediction Summary")

summary = f"""
Category : {category}

Brand : {brand}

Payment Mode : {payment}

Month : {month}

Quantity : {quantity}

Selling Price : ₹{selling_price}

Cost Price : ₹{cost_price}

Predicted Revenue : ₹{prediction[0]:,.2f}

Estimated Profit : ₹{profit:,.2f}
"""

st.code(summary)
# =====================================
# ANALYTICS DASHBOARD
# =====================================

st.markdown("---")

st.header("📊 Retail Analytics Dashboard")

tab1, tab2, tab3, tab4 = st.tabs([
    "Revenue by Category",
    "Payment Modes",
    "Top Brands",
    "Monthly Sales"
])

# -------------------------
# Revenue by Category
# -------------------------

with tab1:

    revenue_category = (
        df.groupby("Category")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        revenue_category,
        x="Category",
        y="Revenue",
        color="Revenue",
        title="Revenue by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Payment Mode
# -------------------------

with tab2:

    payment = (
        df["Payment_Mode"]
        .value_counts()
        .reset_index()
    )

    payment.columns = ["Payment Mode","Count"]

    fig = px.pie(
        payment,
        names="Payment Mode",
        values="Count",
        title="Payment Mode Distribution",
        hole=0.45
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Top Brands
# -------------------------

with tab3:

    brands = (
        df.groupby("Brand")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        brands,
        x="Brand",
        y="Revenue",
        color="Revenue",
        title="Top Revenue Generating Brands"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Monthly Sales
# -------------------------

with tab4:

    month_sales = (
        df.groupby("Month")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        month_sales,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue Trend"
    )

    st.plotly_chart(fig, use_container_width=True)
    # =====================================
# DOWNLOAD PREDICTION REPORT
# =====================================

st.markdown("---")

st.header("📥 Download Prediction Report")

# Create prediction report only after prediction
try:
    report = pd.DataFrame({
        "Category":[category],
        "Brand":[brand],
        "Payment Mode":[payment],
        "Month":[month],
        "Quantity":[quantity],
        "Selling Price":[selling_price],
        "Cost Price":[cost_price],
        "Predicted Revenue":[round(float(prediction[0]),2)],
        "Estimated Profit":[round(float(profit),2)]
    })

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download CSV Report",
        data=csv,
        file_name="RetailIQ_Prediction_Report.csv",
        mime="text/csv"
    )

except:
    st.info("Generate a prediction first to download the report.")
    # =====================================
# FOOTER
# =====================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:20px">

<h3>🛒 RetailIQ AI</h3>

AI Powered Retail Revenue Prediction System

<br>

Developed by <b>Jenifer R</b>

<br><br>

Powered by

Python • Streamlit • Scikit-Learn • Pandas • Power BI

<br><br>

© 2026 RetailIQ AI

</div>
""",
unsafe_allow_html=True
)