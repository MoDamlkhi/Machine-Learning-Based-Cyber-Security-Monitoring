import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(
    layout="wide",
    page_title="IDS Dashboard | Enterprise Security",
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# ==========================
# OPTIMIZED PROFESSIONAL UI STYLES
# ==========================

st.markdown("""
<style>
    /* Modern Professional Theme - Optimized */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Main Background - Simplified */
    .stApp {
        background: linear-gradient(135deg, #0A0F2E 0%, #070B1A 100%);
    }
    
    /* Premium Login Container - Optimized */
    .login-wrapper {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
    }
    
    .login-card {
        max-width: 480px;
        width: 100%;
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 32px;
        padding: 2.5rem;
        border: 1px solid rgba(79, 70, 229, 0.3);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }
    
    /* Logo Section */
    .logo-section {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .logo-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        display: inline-block;
    }
    
    .logo-title {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .logo-badge {
        display: inline-block;
        background: rgba(79, 70, 229, 0.2);
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.7rem;
        color: #A5B4FC;
        border: 1px solid rgba(79, 70, 229, 0.3);
    }
    
    /* Input Fields - Optimized */
    .input-group {
        margin-bottom: 1.5rem;
    }
    
    .input-label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #94A3B8;
        font-size: 0.875rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .stTextInput {
        width: 100%;
    }
    
    .stTextInput > div > div > input {
        background: rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(79, 70, 229, 0.3);
        border-radius: 16px;
        padding: 0.8rem 1rem;
        color: #F1F5F9;
        font-size: 0.95rem;
        transition: all 0.2s ease;
        width: 100%;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #4F46E5;
        box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.2);
        background: rgba(0, 0, 0, 0.4);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #4B5563;
    }
    
    /* Login Button - Optimized */
    .login-btn-wrapper {
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Additional Options */
    .additional-options {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 1.5rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(79, 70, 229, 0.2);
    }
    
    .security-badge {
        color: #64748B;
        font-size: 0.75rem;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .help-link {
        color: #818CF8;
        font-size: 0.75rem;
        text-decoration: none;
        cursor: pointer;
    }
    
    .help-link:hover {
        color: #A5B4FC;
    }
    
    /* Premium Header */
    .premium-header {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(6, 182, 212, 0.05));
        backdrop-filter: blur(5px);
        border-radius: 24px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(79, 70, 229, 0.2);
    }
    
    .header-title {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #FFFFFF, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Premium Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(10, 15, 46, 0.9));
        backdrop-filter: blur(5px);
        border-radius: 20px;
        padding: 1.5rem;
        border: 1px solid rgba(79, 70, 229, 0.3);
        transition: transform 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-3px);
    }
    
    .metric-icon {
        font-size: 1.8rem;
        margin-bottom: 0.8rem;
    }
    
    .metric-label {
        color: #94A3B8;
        font-size: 0.85rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0.5rem 0;
        background: linear-gradient(135deg, #FFFFFF, #A5B4FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Threat Badges */
    .threat-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.875rem;
    }
    
    .threat-critical {
        background: rgba(239, 68, 68, 0.2);
        border: 1px solid #EF4444;
        color: #FECACA;
    }
    
    .threat-high {
        background: rgba(245, 158, 11, 0.2);
        border: 1px solid #F59E0B;
        color: #FDE68A;
    }
    
    .threat-medium {
        background: rgba(59, 130, 246, 0.2);
        border: 1px solid #3B82F6;
        color: #BFDBFE;
    }
    
    .threat-low {
        background: rgba(16, 185, 129, 0.2);
        border: 1px solid #10B981;
        color: #A7F3D0;
    }
    
    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: rgba(10, 15, 46, 0.5);
        border-radius: 12px;
        padding: 0.25rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        color: white;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: rgba(10, 15, 46, 0.95);
        backdrop-filter: blur(5px);
        border-right: 1px solid rgba(79, 70, 229, 0.2);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.2s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 5px 15px rgba(79, 70, 229, 0.3);
    }
    
    /* File Uploader */
    .stFileUploader {
        border: 2px dashed #4F46E5;
        border-radius: 15px;
        padding: 1.5rem;
        background: rgba(79, 70, 229, 0.05);
    }
    
    /* Dataframe */
    .dataframe {
        border-radius: 12px;
        overflow: hidden;
    }
    
    .dataframe thead th {
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        color: white;
        padding: 12px;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0A0F2E;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #4F46E5;
        border-radius: 3px;
    }
    
    /* Success/Warning/Error Boxes */
    .stAlert {
        border-radius: 12px;
        border-left: 4px solid;
    }
</style>
""", unsafe_allow_html=True)

# ==========================
# OPTIMIZED PROFESSIONAL LOGIN UI
# ==========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    # Create a centered container for login
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="login-wrapper">
            <div class="login-card">
                <div class="logo-section">
                    <div class="logo-icon">🛡️</div>
                    <div class="logo-title">IDS Guardian</div>
                    <div class="logo-badge">Enterprise Security Platform</div>
                </div>
        """, unsafe_allow_html=True)
        
        # Username field
        st.markdown("""
        <div class="input-group">
            <div class="input-label">
                <span>👤</span>
                <span>Username</span>
            </div>
        """, unsafe_allow_html=True)
        username = st.text_input("", placeholder="Enter your username", key="login_username", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Password field
        st.markdown("""
        <div class="input-group">
            <div class="input-label">
                <span>🔒</span>
                <span>Password</span>
            </div>
        """, unsafe_allow_html=True)
        password = st.text_input("", type="password", placeholder="Enter your password", key="login_password", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Login button
        st.markdown('<div class="login-btn-wrapper">', unsafe_allow_html=True)
        if st.button("🔐 Sign In", use_container_width=True, key="login_button"):
            # Original login logic - NO CHANGES
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("✓ Authentication successful")
                st.balloons()
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("✗ Invalid credentials. Please try again.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Additional options
        st.markdown("""
        <div class="additional-options">
            <span class="security-badge">
                🔒 Secure Enterprise Access
            </span>
            <span class="help-link">
                Need help?
            </span>
        </div>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.stop()

# ==========================
# PREMIUM DASHBOARD HEADER
# ==========================

st.markdown("""
<div class="premium-header">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
        <div>
            <div class="header-title">
                🚨 Real-Time Intrusion Detection Dashboard
            </div>
            <p style="color: #94A3B8; margin-top: 0.25rem;">
                Advanced Threat Monitoring & Analysis Platform
            </p>
        </div>
        <div class="threat-badge threat-low">
            <span>🟢</span>
            <span>System Operational</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================
# LOAD MODEL (CACHED)
# ==========================

@st.cache_resource
def load_models():
    model = joblib.load("ids_model.pkl")
    features = joblib.load("feature_names.pkl")
    return model, features

model, features = load_models()

# ==========================
# PREMIUM SIDEBAR
# ==========================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div style="font-size: 3rem;">🛡️</div>
        <h3 style="margin: 0.5rem 0; background: linear-gradient(135deg, #FFFFFF, #818CF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            IDS Guardian
        </h3>
        <p style="color: #64748B; font-size: 0.8rem;">Real-time Threat Detection</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    uploaded_file = st.file_uploader("📂 Upload Network CSV Dataset", type=["csv"], help="Upload CSV file with network traffic features")
    
    if uploaded_file:
        st.success("✅ Dataset loaded successfully")
    
    st.markdown("---")
    
    with st.expander("ℹ️ System Information"):
        st.markdown(f"""
        - **Model:** Random Forest Classifier
        - **Features:** {len(features)} dimensions
        - **Status:** Active
        - **Last Updated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
        """)
    
    st.markdown("---")
    
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

# ==========================
# MAIN CONTENT
# ==========================

if uploaded_file:
    # Load and process data
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()
    
    st.toast("Dataset loaded successfully 🚀")
    st.success("✅ Dataset Loaded Successfully")
    st.info(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    
    # Preprocessing
    df = df.reindex(columns=features, fill_value=0)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)
    
    # Prediction
    with st.spinner("🔄 Analyzing network traffic..."):
        prediction = model.predict(df)
    
    df["Prediction"] = prediction
    
    # Statistics
    attack_count = (df["Prediction"] == 1).sum()
    benign_count = (df["Prediction"] == 0).sum()
    total = len(df)
    attack_rate = (attack_count / total) * 100 if total > 0 else 0
    
    # ==========================
    # METRICS DISPLAY
    # ==========================
    
    st.subheader("📊 Security Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="text-align: center;">
            <div class="metric-icon">📊</div>
            <div class="metric-label">Total Flows</div>
            <div class="metric-value">{total:,}</div>
            <div style="color: #10B981; font-size: 0.75rem;">Current Session</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="text-align: center;">
            <div class="metric-icon">⚠️</div>
            <div class="metric-label">Attacks Detected</div>
            <div class="metric-value" style="background: linear-gradient(135deg, #EF4444, #DC2626); -webkit-background-clip: text;">{attack_count:,}</div>
            <div style="color: #EF4444; font-size: 0.75rem;">Threats Found</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card" style="text-align: center;">
            <div class="metric-icon">✅</div>
            <div class="metric-label">Benign Traffic</div>
            <div class="metric-value" style="background: linear-gradient(135deg, #10B981, #059669); -webkit-background-clip: text;">{benign_count:,}</div>
            <div style="color: #10B981; font-size: 0.75rem;">Safe Connections</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        risk_class = "threat-critical" if attack_rate > 50 else "threat-high" if attack_rate > 30 else "threat-medium" if attack_rate > 10 else "threat-low"
        st.markdown(f"""
        <div class="metric-card" style="text-align: center;">
            <div class="metric-icon">🎯</div>
            <div class="metric-label">Attack Rate</div>
            <div class="metric-value">{attack_rate:.1f}%</div>
            <div class="{risk_class}" style="display: inline-block; margin-top: 0.25rem; padding: 0.25rem 0.75rem;">RISK</div>
        </div>
        """, unsafe_allow_html=True)
    
    # ==========================
    # SMART INSIGHTS
    # ==========================
    
    st.subheader("🧠 AI Insights")
    
    if attack_rate > 50:
        st.error("⚠️ Critical Threat Level: Immediate action required!")
    elif attack_rate > 30:
        st.warning("⚠️ High suspicious activity detected.")
    elif attack_rate > 10:
        st.info("ℹ️ Moderate anomalies detected.")
    else:
        st.success("✅ Network traffic is mostly safe.")
    
    # Risk indicator
    if attack_rate > 30:
        st.error("🔴 HIGH RISK DETECTED")
    elif attack_rate > 10:
        st.warning("🟠 MEDIUM RISK")
    else:
        st.success("🟢 NETWORK SAFE")
    
    # ==========================
    # CHARTS
    # ==========================
    
    col1, col2 = st.columns(2)
    
    with col1:
        pie = px.pie(
            values=[benign_count, attack_count],
            names=["Benign", "Attack"],
            color=["Benign", "Attack"],
            color_discrete_map={"Benign": "#10B981", "Attack": "#EF4444"},
            title="Traffic Distribution",
            hole=0.4
        )
        pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#F1F5F9", size=11),
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(pie, use_container_width=True, config={'displayModeBar': False})
    
    with col2:
        bar = px.bar(
            x=["Benign", "Attack"],
            y=[benign_count, attack_count],
            title="Detection Results",
            color=["Benign", "Attack"],
            color_discrete_map={"Benign": "#10B981", "Attack": "#EF4444"},
            text_auto=True
        )
        bar.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#F1F5F9", size=11),
            margin=dict(l=20, r=20, t=40, b=20)
        )
        bar.update_traces(textfont_color="white", textposition="outside")
        st.plotly_chart(bar, use_container_width=True, config={'displayModeBar': False})
    
    # ==========================
    # GAUGE
    # ==========================
    
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=attack_rate,
        title={'text': "Attack Percentage", 'font': {'size': 16, 'color': "#F1F5F9"}},
        gauge={
            'axis': {'range': [0, 100], 'tickcolor': "#F1F5F9"},
            'bar': {'color': "#EF4444"},
            'bgcolor': "rgba(255,255,255,0.05)",
            'steps': [
                {'range': [0, 30], 'color': "rgba(16, 185, 129, 0.2)"},
                {'range': [30, 70], 'color': "rgba(245, 158, 11, 0.2)"},
                {'range': [70, 100], 'color': "rgba(239, 68, 68, 0.2)"}
            ]
        }
    ))
    gauge.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F1F5F9"),
        height=350,
        margin=dict(l=30, r=30, t=50, b=30)
    )
    st.plotly_chart(gauge, use_container_width=True, config={'displayModeBar': False})
    
    # ==========================
    # TREND CHART
    # ==========================
    
    trend = df["Prediction"].value_counts().reset_index()
    trend.columns = ["Type", "Count"]
    trend["Type"] = trend["Type"].map({0: "Benign", 1: "Attack"})
    
    fig = px.line(
        trend,
        x="Type",
        y="Count",
        title="Attack Trend Overview",
        markers=True
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F1F5F9", size=11),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    fig.update_traces(line_color="#4F46E5", marker_color="#06B6D4")
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # ==========================
    # TABLE
    # ==========================
    
    st.subheader("🔍 Prediction Results")
    st.dataframe(df.head(50), use_container_width=True)
    
    # ==========================
    # DOWNLOAD
    # ==========================
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Results as CSV",
        data=csv,
        file_name=f"prediction_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

else:
    st.info("⬆️ Upload a dataset to start analysis")
