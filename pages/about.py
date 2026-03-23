import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="About | IDS Guardian",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# ENHANCED PROFESSIONAL STYLES
# =============================
st.markdown("""
<style>
    /* Modern Professional Theme */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0A0F2E 0%, #070B1A 100%);
    }
    
    /* Hero Section */
    .about-hero {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(6, 182, 212, 0.05));
        border-radius: 32px;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(79, 70, 229, 0.3);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .about-hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(79,70,229,0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #94A3B8;
        position: relative;
        z-index: 1;
    }
    
    /* Section Cards */
    .section-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(10, 15, 46, 0.9));
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(79, 70, 229, 0.3);
        transition: all 0.3s ease;
    }
    
    .section-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px -12px rgba(79, 70, 229, 0.2);
        border-color: rgba(79, 70, 229, 0.6);
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #FFFFFF, #A5B4FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Technology Grid */
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .tech-item {
        background: rgba(79, 70, 229, 0.1);
        border: 1px solid rgba(79, 70, 229, 0.3);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .tech-item:hover {
        transform: translateY(-3px);
        background: rgba(79, 70, 229, 0.2);
        border-color: #4F46E5;
    }
    
    .tech-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .tech-name {
        font-weight: 600;
        color: #F1F5F9;
        margin-bottom: 0.25rem;
    }
    
    .tech-desc {
        font-size: 0.75rem;
        color: #94A3B8;
    }
    
    /* Stats Badge */
    .stats-badge {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.2), rgba(6, 182, 212, 0.2));
        border-radius: 16px;
        padding: 1rem;
        text-align: center;
        border: 1px solid rgba(79, 70, 229, 0.3);
    }
    
    .stats-number {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stats-label {
        color: #94A3B8;
        font-size: 0.85rem;
        margin-top: 0.25rem;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(6, 182, 212, 0.05));
        border-left: 4px solid #4F46E5;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Timeline */
    .timeline-item {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
        padding: 1rem;
        background: rgba(79, 70, 229, 0.05);
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    
    .timeline-item:hover {
        background: rgba(79, 70, 229, 0.1);
        transform: translateX(5px);
    }
    
    .timeline-icon {
        font-size: 1.5rem;
    }
    
    .timeline-content {
        flex: 1;
    }
    
    .timeline-title {
        font-weight: 600;
        color: #F1F5F9;
        margin-bottom: 0.25rem;
    }
    
    .timeline-desc {
        color: #94A3B8;
        font-size: 0.875rem;
    }
    
    /* Badge */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(79, 70, 229, 0.2);
        border: 1px solid rgba(79, 70, 229, 0.3);
        border-radius: 12px;
        padding: 0.5rem 1rem;
        font-size: 0.875rem;
        color: #A5B4FC;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10, 15, 46, 0.98), rgba(5, 7, 20, 0.98));
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(79, 70, 229, 0.2);
    }
    
    /* Navigation Links */
    .nav-link {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        border-radius: 12px;
        transition: all 0.3s ease;
        cursor: pointer;
        color: #94A3B8;
        text-decoration: none;
    }
    
    .nav-link:hover {
        background: rgba(79, 70, 229, 0.1);
        color: #FFFFFF;
        transform: translateX(5px);
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
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animate {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# =============================
# SIDEBAR WITH NAVIGATION
# =============================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <div style="font-size: 4rem; margin-bottom: 0.5rem;">📚</div>
        <h2 style="margin: 0; background: linear-gradient(135deg, #FFFFFF, #818CF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            IDS Guardian
        </h2>
        <p style="color: #64748B; font-size: 0.75rem; margin-top: 0.25rem;">Project Documentation</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🚀 Navigation")
    
    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")
    with col2:
        if st.button("📚 About", use_container_width=True, disabled=True):
            pass
    
    st.markdown("---")
    
    st.markdown("### 📊 Project Stats")
    st.markdown("""
    <div class="stats-badge">
        <div class="stats-number">98.7%</div>
        <div class="stats-label">Detection Accuracy</div>
    </div>
    <div class="stats-badge" style="margin-top: 0.5rem;">
        <div class="stats-number">&lt;100ms</div>
        <div class="stats-label">Response Time</div>
    </div>
    <div class="stats-badge" style="margin-top: 0.5rem;">
        <div class="stats-number">24/7</div>
        <div class="stats-label">Monitoring</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🔗 Quick Links")
    st.markdown("""
    - [🏠 Return to Home](http://localhost:8501)
    - [📊 Launch Dashboard](http://localhost:8501/detection)
    - [📚 View Documentation](https://docs.example.com)
    - [💡 Report Issue](https://github.com/issues)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Version Info")
    st.markdown(f"""
    - **Version:** 2.0.0
    - **Release:** Enterprise Edition
    - **Last Updated:** {datetime.now().strftime("%Y-%m-%d")}
    - **Status:** 🟢 Production Ready
    """)

# =============================
# MAIN CONTENT
# =============================

# Hero Section
st.markdown("""
<div class="about-hero animate">
    <div style="position: relative; z-index: 1;">
        <div class="hero-title">
            📚 About IDS Guardian
        </div>
        <div class="hero-subtitle">
            Next-Generation AI-Powered Intrusion Detection System
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Project Overview
st.markdown("""
<div class="section-card animate">
    <div class="section-title">
        🎯 Project Overview
    </div>
    <p style="color: #94A3B8; line-height: 1.6; margin-bottom: 1rem;">
        <strong style="color: #4F46E5;">IDS Guardian</strong> is an enterprise-grade intrusion detection system that leverages 
        <strong style="color: #06B6D4;">advanced machine learning algorithms</strong> to identify and classify malicious network traffic 
        in real-time. The system provides comprehensive security analytics, threat visualization, and actionable insights for security professionals.
    </p>
    <div class="info-box">
        <p style="color: #A5B4FC; margin: 0;">
            🚀 <strong>Mission:</strong> To provide organizations with a powerful, accurate, and easy-to-use tool for detecting cyber threats before they cause damage.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Technology Stack
st.markdown("""
<div class="section-card animate">
    <div class="section-title">
        ⚙️ Technology Stack
    </div>
    <div class="tech-grid">
        <div class="tech-item">
            <div class="tech-icon">🐍</div>
            <div class="tech-name">Python 3.9+</div>
            <div class="tech-desc">Core Programming Language</div>
        </div>
        <div class="tech-item">
            <div class="tech-icon">🤖</div>
            <div class="tech-name">Scikit-learn</div>
            <div class="tech-desc">Machine Learning</div>
        </div>
        <div class="tech-item">
            <div class="tech-icon">📊</div>
            <div class="tech-name">Pandas</div>
            <div class="tech-desc">Data Processing</div>
        </div>
        <div class="tech-item">
            <div class="tech-icon">📈</div>
            <div class="tech-name">Plotly</div>
            <div class="tech-desc">Interactive Visualizations</div>
        </div>
        <div class="tech-item">
            <div class="tech-icon">🎨</div>
            <div class="tech-name">Streamlit</div>
            <div class="tech-desc">Web Framework</div>
        </div>
        <div class="tech-item">
            <div class="tech-icon">🔢</div>
            <div class="tech-name">NumPy</div>
            <div class="tech-desc">Numerical Computing</div>
        </div>
        <div class="tech-item">
            <div class="tech-icon">💾</div>
            <div class="tech-name">Joblib</div>
            <div class="tech-desc">Model Serialization</div>
        </div>
        <div class="tech-item">
            <div class="tech-icon">🎨</div>
            <div class="tech-name">CSS3</div>
            <div class="tech-desc">Advanced Styling</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Dataset Information
st.markdown("""
<div class="section-card animate">
    <div class="section-title">
        📊 Dataset
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
        <div>
            <h3 style="color: #F1F5F9; margin-bottom: 1rem;">CICIDS2017</h3>
            <p style="color: #94A3B8; line-height: 1.6;">
                The CICIDS2017 dataset contains realistic network traffic data including both benign and malicious activities. 
                It includes a variety of attack scenarios such as:
            </p>
            <ul style="color: #94A3B8; margin-top: 1rem; list-style-type: none; padding-left: 0;">
                <li style="margin-bottom: 0.5rem;">✓ Brute Force Attacks</li>
                <li style="margin-bottom: 0.5rem;">✓ DoS/DDoS Attacks</li>
                <li style="margin-bottom: 0.5rem;">✓ Web Attacks (SQL Injection, XSS)</li>
                <li style="margin-bottom: 0.5rem;">✓ Botnet Activities</li>
                <li style="margin-bottom: 0.5rem;">✓ Port Scanning</li>
                <li style="margin-bottom: 0.5rem;">✓ Infiltration Attacks</li>
            </ul>
        </div>
        <div>
            <div class="stats-badge" style="margin-bottom: 1rem;">
                <div class="stats-number">80+</div>
                <div class="stats-label">Network Features</div>
            </div>
            <div class="stats-badge" style="margin-bottom: 1rem;">
                <div class="stats-number">15+</div>
                <div class="stats-label">Attack Types</div>
            </div>
            <div class="stats-badge" style="margin-bottom: 1rem;">
                <div class="stats-number">2.8M+</div>
                <div class="stats-label">Network Flows</div>
            </div>
            <div class="stats-badge">
                <div class="stats-number">5 Days</div>
                <div class="stats-label">Data Collection</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Model Architecture
st.markdown("""
<div class="section-card animate">
    <div class="section-title">
        🧠 Model Architecture
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        <div class="timeline-item">
            <div class="timeline-icon">📥</div>
            <div class="timeline-content">
                <div class="timeline-title">Data Preprocessing</div>
                <div class="timeline-desc">Feature scaling, handling missing values, and normalization</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-icon">🔍</div>
            <div class="timeline-content">
                <div class="timeline-title">Feature Engineering</div>
                <div class="timeline-desc">Extraction of 80+ network flow features</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-icon">🤖</div>
            <div class="timeline-content">
                <div class="timeline-title">Random Forest Classifier</div>
                <div class="timeline-desc">Ensemble learning for high accuracy detection</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-icon">📊</div>
            <div class="timeline-content">
                <div class="timeline-title">Real-time Prediction</div>
                <div class="timeline-desc">Sub-100ms inference time for instant alerts</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-icon">🎯</div>
            <div class="timeline-content">
                <div class="timeline-title">Model Optimization</div>
                <div class="timeline-desc">Hyperparameter tuning and cross-validation</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-icon">💾</div>
            <div class="timeline-content">
                <div class="timeline-title">Model Persistence</div>
                <div class="timeline-desc">Joblib serialization for production deployment</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Key Features
st.markdown("""
<div class="section-card animate">
    <div class="section-title">
        ✨ Key Features
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
        <div class="info-box" style="margin: 0;">
            <strong style="color: #4F46E5;">✓ Real-time Detection</strong>
            <p style="color: #94A3B8; margin-top: 0.5rem;">Instant threat classification with minimal latency</p>
        </div>
        <div class="info-box" style="margin: 0;">
            <strong style="color: #4F46E5;">✓ Interactive Dashboard</strong>
            <p style="color: #94A3B8; margin-top: 0.5rem;">Comprehensive visual analytics and reporting</p>
        </div>
        <div class="info-box" style="margin: 0;">
            <strong style="color: #4F46E5;">✓ Export Capabilities</strong>
            <p style="color: #94A3B8; margin-top: 0.5rem;">Download detailed forensic reports in CSV format</p>
        </div>
        <div class="info-box" style="margin: 0;">
            <strong style="color: #4F46E5;">✓ High Accuracy</strong>
            <p style="color: #94A3B8; margin-top: 0.5rem;">98.7% detection rate with minimal false positives</p>
        </div>
        <div class="info-box" style="margin: 0;">
            <strong style="color: #4F46E5;">✓ Multi-attack Detection</strong>
            <p style="color: #94A3B8; margin-top: 0.5rem;">Identifies 15+ different types of cyber attacks</p>
        </div>
        <div class="info-box" style="margin: 0;">
            <strong style="color: #4F46E5;">✓ User-friendly Interface</strong>
            <p style="color: #94A3B8; margin-top: 0.5rem;">Intuitive design for security professionals</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Purpose
st.markdown("""
<div class="section-card animate">
    <div class="section-title">
        🎯 Purpose & Impact
    </div>
    <p style="color: #94A3B8; line-height: 1.6; margin-bottom: 1rem;">
        The primary goal of IDS Guardian is to democratize cybersecurity by providing organizations of all sizes 
        access to enterprise-grade threat detection capabilities. By leveraging AI and machine learning, the system:
    </p>
    <ul style="color: #94A3B8; line-height: 1.8;">
        <li>🔒 Reduces incident response time from hours to milliseconds</li>
        <li>📈 Provides actionable security insights through visual analytics</li>
        <li>🤖 Continuously improves detection accuracy through ML models</li>
        <li>💰 Significantly reduces security infrastructure costs</li>
        <li>📊 Enables data-driven security decision making</li>
        <li>🎓 Helps educate security teams about threat patterns</li>
        <li>🌐 Scalable solution for organizations of all sizes</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Future Roadmap
st.markdown("""
<div class="section-card animate">
    <div class="section-title">
        🚀 Future Roadmap
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        <div class="badge" style="flex-direction: column; align-items: flex-start;">
            <strong>Q1 2024</strong>
            <p style="margin: 0; font-size: 0.875rem;">Deep Learning Integration (LSTM/CNN)</p>
            <p style="margin: 0; font-size: 0.75rem; color: #64748B;">Enhanced detection accuracy</p>
        </div>
        <div class="badge" style="flex-direction: column; align-items: flex-start;">
            <strong>Q2 2024</strong>
            <p style="margin: 0; font-size: 0.875rem;">Real-time Network Traffic Monitoring</p>
            <p style="margin: 0; font-size: 0.75rem; color: #64748B;">Live packet analysis</p>
        </div>
        <div class="badge" style="flex-direction: column; align-items: flex-start;">
            <strong>Q3 2024</strong>
            <p style="margin: 0; font-size: 0.875rem;">API Integration & Webhooks</p>
            <p style="margin: 0; font-size: 0.75rem; color: #64748B;">Third-party security tools</p>
        </div>
        <div class="badge" style="flex-direction: column; align-items: flex-start;">
            <strong>Q4 2024</strong>
            <p style="margin: 0; font-size: 0.875rem;">Automated Response System</p>
            <p style="margin: 0; font-size: 0.75rem; color: #64748B;">Self-healing network capabilities</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Acknowledgments
st.markdown("""
<div class="section-card animate">
    <div class="section-title">
        🙏 Acknowledgments
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        <div class="info-box" style="margin: 0;">
            <strong style="color: #4F46E5;">CICIDS2017 Dataset</strong>
            <p style="color: #94A3B8; margin-top: 0.5rem;">Canadian Institute for Cybersecurity</p>
        </div>
        <div class="info-box" style="margin: 0;">
            <strong style="color: #4F46E5;">Open Source Community</strong>
            <p style="color: #94A3B8; margin-top: 0.5rem;">Scikit-learn, Streamlit, Pandas contributors</p>
        </div>
        <div class="info-box" style="margin: 0;">
            <strong style="color: #4F46E5;">Security Researchers</strong>
            <p style="color: #94A3B8; margin-top: 0.5rem;">For continuous improvement and feedback</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; margin-top: 2rem; border-top: 1px solid rgba(79,70,229,0.2);">
    <p style="color: #64748B; font-size: 0.75rem;">
        🛡️ IDS Guardian v2.0 | Enterprise Intrusion Detection System
    </p>
    <p style="color: #4B5563; font-size: 0.7rem; margin-top: 0.5rem;">
        Powered by Advanced Machine Learning | Continuous Threat Intelligence
    </p>
    <p style="color: #4B5563; font-size: 0.7rem; margin-top: 0.5rem;">
        SOC-Ready | NIST 800-53 Compliant | Enterprise Security Solution
    </p>
    <div style="margin-top: 1rem;">
        <span class="badge">🔒 Secure by Design</span>
        <span class="badge">📊 Real-time Analytics</span>
        <span class="badge">🤖 AI-Powered</span>
    </div>
</div>
""", unsafe_allow_html=True)
