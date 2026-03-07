import streamlit as st

st.set_page_config(
    page_title="AI Intrusion Detection System",
    page_icon="🛡️",
    layout="wide"
)

# =============================
# STYLE
# =============================
st.markdown("""
<style>

body {
background-color:#0E1117;
}

.big-title{
font-size:48px;
font-weight:bold;
text-align:center;
}

.subtitle{
font-size:22px;
text-align:center;
color:gray;
}

.box{
background-color:#1A1D24;
padding:30px;
border-radius:10px;
border:1px solid #2E2E38;
}

</style>
""", unsafe_allow_html=True)

# =============================
# HEADER
# =============================

st.markdown("<p class='big-title'>🛡️ AI Network Intrusion Detection System</p>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Machine Learning Based Cyber Security Monitoring</p>", unsafe_allow_html=True)

st.write("")

# =============================
# DESCRIPTION
# =============================

st.markdown("""
### 🔎 What This System Does

This platform analyzes **network traffic datasets** and automatically detects cyber attacks using **machine learning algorithms**.

The system is designed to help security analysts identify malicious traffic quickly.
""")

st.write("")

# =============================
# FEATURES
# =============================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📂 Upload Dataset
    Upload network traffic CSV file for analysis
    """)

with col2:
    st.markdown("""
    ### 🤖 AI Detection
    Machine learning model classifies traffic
    """)

with col3:
    st.markdown("""
    ### 📊 Security Dashboard
    Visualize attack statistics and risk levels
    """)

st.write("")

st.info("Use the **left sidebar** to open the Detection Dashboard.")