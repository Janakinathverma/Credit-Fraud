import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from queries import (
    QUERY_DONUT, QUERY_HIST, QUERY_FRAUD_COUNT, QUERY_FRAUD_PERCENT, 
    QUERY_TOTAL, QUERY_AVG_AMOUNT, QUERY_MAX_FRAUD, QUERY_TIME_TREND
)

# Page Configuration
st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide", page_icon="🛡️")

# Database Connection
engine = create_engine('sqlite:///database/fraud_data.db')

@st.cache_data(ttl=300)
def fetch_data(query):
    return pd.read_sql(query, engine)

# Futuristic UI Styling
st.markdown("""
    <style>
    .main { background: #0c0c0c; color: #e0e0e0; }
    h1 { color: #00d4ff; text-align: center; font-family: sans-serif; }
    .metric-container { background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 10px; border: 1px solid #333; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ FRAUD DETECTION DASHBOARD v2.0")

# 1. KPI Metrics
total_txn = fetch_data(QUERY_TOTAL).iloc[0, 0]
fraud_cases = fetch_data(QUERY_FRAUD_COUNT).iloc[0, 0]
fraud_pct = fetch_data(QUERY_FRAUD_PERCENT).iloc[0, 0]
max_fraud = fetch_data(QUERY_MAX_FRAUD).iloc[0, 0]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Transactions", f"{total_txn:,}")
c2.metric("Fraud Cases", f"{fraud_cases:,}")
c3.metric("Fraud Rate", f"{fraud_pct:.4f}%")
c4.metric("Max Fraud Amt", f"₹{max_fraud:,.2f}")

st.divider()

# 2. Charts with Insights
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 Class Imbalance")
    fig1 = px.pie(fetch_data(QUERY_DONUT), values='count', names='Class', hole=0.4, 
                  color_discrete_sequence=['#4ecdc4', '#ff6b6b'])
    st.plotly_chart(fig1, use_container_width=True)
    st.success("Insight: The severe imbalance indicates that standard accuracy is a poor metric. F1-Score or AUPRC is required.")

with col2:
    st.subheader("💹 Amount Distribution")
    fig2 = px.histogram(fetch_data(QUERY_HIST), x="Amount", color="Class", log_y=True, 
                        color_discrete_sequence=['#4ecdc4', '#ff6b6b'])
    st.plotly_chart(fig2, use_container_width=True)
    st.warning("Insight: Fraudulent transactions are skewed towards lower values, making them distinct from legitimate spikes.")

# 3. Time Trend
st.subheader("⏱️ Temporal Patterns")
fig3 = px.scatter(fetch_data(QUERY_TIME_TREND), x="Time", y="Amount", color="Class")
st.plotly_chart(fig3, use_container_width=True)
st.info("Insight: Time-based clusters suggest cyclical fraud patterns, enabling us to engineer 'Hour-of-Day' features for better prediction.")