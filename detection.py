import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("🚨 Intrusion Detection Dashboard")

# ==========================
# Load Model
# ==========================

model = joblib.load("ids_model.pkl")
features = joblib.load("feature_names.pkl")

# ==========================
# Upload Dataset
# ==========================

uploaded_file = st.file_uploader("Upload Network CSV Dataset", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    df.columns = df.columns.str.strip()

    st.success("Dataset Loaded Successfully")

    # ==========================
    # Feature Alignment
    # ==========================

    df = df.reindex(columns=features, fill_value=0)

    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    df.fillna(0, inplace=True)

    # ==========================
    # Prediction
    # ==========================

    prediction = model.predict(df)

    df["Prediction"] = prediction

    # ==========================
    # Statistics
    # ==========================

    attack_count = (df["Prediction"] == 1).sum()

    benign_count = (df["Prediction"] == 0).sum()

    total = len(df)

    attack_rate = (attack_count / total) * 100

    # ==========================
    # Dashboard Metrics
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Flows", total)

    col2.metric("Attacks Detected", attack_count)

    col3.metric("Benign Traffic", benign_count)

    col4.metric("Attack Rate", f"{attack_rate:.2f}%")

    # ==========================
    # Risk Indicator
    # ==========================

    if attack_rate > 30:

        st.error("🔴 High Network Risk")

    elif attack_rate > 10:

        st.warning("🟠 Medium Network Risk")

    else:

        st.success("🟢 Network Appears Safe")

    # ==========================
    # Charts
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        pie = px.pie(
            values=[benign_count, attack_count],
            names=["Benign", "Attack"],
            title="Traffic Distribution"
        )

        st.plotly_chart(pie, use_container_width=True)

    with col2:

        bar = px.bar(
            x=["Benign", "Attack"],
            y=[benign_count, attack_count],
            title="Detection Results"
        )

        st.plotly_chart(bar, use_container_width=True)

    # ==========================
    # Gauge
    # ==========================

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=attack_rate,
        title={'text': "Attack Percentage"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "red"}
        }
    ))

    st.plotly_chart(gauge, use_container_width=True)

    # ==========================
    # Table
    # ==========================

    st.subheader("Prediction Results")

    st.dataframe(df.head(50))

else:

    st.info("Upload a dataset to start analysis")