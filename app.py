import streamlit as st
import time

st.set_page_config(
    page_title="AI Intrusion Detection System | Enterprise Security",
    page_icon="🛡️",
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
    .hero-section {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(6, 182, 212, 0.05));
        border-radius: 32px;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(79, 70, 229, 0.3);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
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
    
    .big-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #94A3B8;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }
    
    /* Feature Cards Premium */
    .feature-card-premium {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(10, 15, 46, 0.9));
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2rem;
        border: 1px solid rgba(79, 70, 229, 0.3);
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card-premium::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #4F46E5, #06B6D4);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .feature-card-premium:hover::before {
        transform: scaleX(1);
    }
    
    .feature-card-premium:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px -12px rgba(79, 70, 229, 0.4);
        border-color: rgba(79, 70, 229, 0.6);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #FFFFFF, #A5B4FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .feature-description {
        color: #94A3B8;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    /* Stats Section */
    .stats-section {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.05), rgba(6, 182, 212, 0.05));
        border-radius: 24px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(79, 70, 229, 0.2);
    }
    
    .stat-card {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: #94A3B8;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Technology Badges */
    .tech-badge {
        background: rgba(79, 70, 229, 0.1);
        border: 1px solid rgba(79, 70, 229, 0.3);
        border-radius: 12px;
        padding: 0.5rem 1rem;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.875rem;
        color: #A5B4FC;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(6, 182, 212, 0.05));
        border-left: 4px solid #4F46E5;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    /* ========== ENHANCED NAVIGATION BUTTONS ========== */
    .nav-button {
        width: 100%;
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(6, 182, 212, 0.05));
        border: 1px solid rgba(79, 70, 229, 0.3);
        border-radius: 14px;
        padding: 0.85rem 1rem;
        margin: 0.6rem 0;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .nav-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .nav-button:hover::before {
        left: 100%;
    }
    
    .nav-button:hover {
        transform: translateX(8px);
        border-color: #4F46E5;
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.2), rgba(6, 182, 212, 0.1));
        box-shadow: 0 5px 20px rgba(79, 70, 229, 0.3);
    }
    
    .nav-button-active {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.25), rgba(6, 182, 212, 0.15));
        border-left: 3px solid #4F46E5;
        border-color: #4F46E5;
        box-shadow: 0 5px 15px rgba(79, 70, 229, 0.2);
        transform: translateX(5px);
    }
    
    .nav-icon {
        font-size: 1.3rem;
        margin-right: 0.75rem;
        display: inline-block;
    }
    
    .nav-text {
        font-weight: 600;
        font-size: 1rem;
        letter-spacing: 0.3px;
    }
    
    .nav-badge {
        background: rgba(79, 70, 229, 0.3);
        border-radius: 20px;
        padding: 0.2rem 0.6rem;
        font-size: 0.7rem;
        margin-left: 0.5rem;
        color: #A5B4FC;
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
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10, 15, 46, 0.98), rgba(5, 7, 20, 0.98));
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(79, 70, 229, 0.2);
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
</style>
""", unsafe_allow_html=True)

# =============================
# NAVIGATION STATE
# =============================

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'app'

def navigate_to(page):
    st.session_state.page = page
    st.rerun()

# =============================
# SIDEBAR - ENHANCED NAVIGATION BUTTONS
# =============================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0 1rem 0;">
        <div style="font-size: 4rem; margin-bottom: 0.5rem;">🛡️</div>
        <h2 style="margin: 0; background: linear-gradient(135deg, #FFFFFF, #818CF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            IDS Guardian
        </h2>
        <p style="color: #64748B; font-size: 0.75rem; margin-top: 0.25rem;">Enterprise Security Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🚀 Navigation")
    
    # App Button (Home)
    if st.session_state.page == 'app':
        st.markdown("""
        <div class="nav-button nav-button-active">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center;">
                    <span class="nav-icon">🏠</span>
                    <span class="nav-text">Home</span>
                </div>
                <span class="nav-badge">Active</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            navigate_to('app')
    
    # About Button
    if st.session_state.page == 'about':
        st.markdown("""
        <div class="nav-button nav-button-active">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center;">
                    <span class="nav-icon">📚</span>
                    <span class="nav-text">About</span>
                </div>
                <span class="nav-badge">Active</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        if st.button("📚 About", key="nav_about", use_container_width=True):
            navigate_to('about')
    
   
    
    # System Status
    st.markdown("### 📊 System Status")
    st.markdown("""
    <div class="tech-badge" style="width: 100%; justify-content: center; margin: 0.5rem 0;">
        🟢 System Online
    </div>
    <div class="tech-badge" style="width: 100%; justify-content: center; margin: 0.5rem 0;">
        🤖 AI Active
    </div>
    <div class="tech-badge" style="width: 100%; justify-content: center; margin: 0.5rem 0;">
        🔒 Secure Connection
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Stats
    st.markdown("### 📈 Live Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Active Sessions", "1", delta="Online")
    with col2:
        st.metric("Threats Blocked", "0", delta="Monitoring")
    
    st.markdown("---")
    
    # Session Info
    st.markdown("### 👤 Session")
    st.info("**User:** Security Admin\n\n**Role:** Security Analyst\n\n**Last Active:** Just now")

# =============================
# MAIN CONTENT BASED ON NAVIGATION
# =============================

if st.session_state.page == 'app':
    # Hero Section
    st.markdown("""
    <div class="hero-section animate">
        <div style="position: relative; z-index: 1;">
            <div class="big-title">
                🛡️ AI Intrusion Detection System
            </div>
            <div class="subtitle">
                Advanced Machine Learning Cyber Security Platform
            </div>
            <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 1rem;">
                <span class="tech-badge">🤖 Machine Learning</span>
                <span class="tech-badge">⚡ Real-time Detection</span>
                <span class="tech-badge">📊 Advanced Analytics</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Description Section
    st.markdown("""
    <div class="info-box animate">
        <h3 style="color: #F1F5F9; margin-bottom: 1rem;">🔎 What This System Does</h3>
        <p style="color: #94A3B8; line-height: 1.6;">
            Analyze <strong style="color: #4F46E5;">network traffic datasets</strong> and detect cyber attacks 
            using <strong style="color: #06B6D4;">AI-powered machine learning models</strong> in real-time.
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1.5rem;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #10B981;">✓</span>
                <span style="color: #94A3B8;">Fast detection</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #10B981;">✓</span>
                <span style="color: #94A3B8;">High accuracy (98.7%)</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #10B981;">✓</span>
                <span style="color: #94A3B8;">Visual analytics dashboard</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #10B981;">✓</span>
                <span style="color: #94A3B8;">Real-time monitoring</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats Section
    st.markdown("""
    <div class="stats-section animate">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">
            <div class="stat-card">
                <div class="stat-number">98.7%</div>
                <div class="stat-label">Detection Accuracy</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">&lt;100ms</div>
                <div class="stat-label">Response Time</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Continuous Monitoring</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">50+</div>
                <div class="stat-label">Attack Patterns</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Features Section
    st.markdown("<h2 style='text-align: center; margin: 2rem 0; color: #F1F5F9;'>✨ Key Features</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card-premium">
            <div class="feature-icon">📂</div>
            <div class="feature-title">Upload Dataset</div>
            <div class="feature-description">
                Easily upload CSV network traffic files for instant analysis. Supports multiple formats and large datasets.
            </div>
            <div style="margin-top: 1rem;">
                <span class="tech-badge">CSV Format</span>
                <span class="tech-badge">Batch Processing</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card-premium">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI Detection</div>
            <div class="feature-description">
                Advanced machine learning algorithms classify network traffic with high precision and minimal false positives.
            </div>
            <div style="margin-top: 1rem;">
                <span class="tech-badge">Random Forest</span>
                <span class="tech-badge">Deep Learning</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card-premium">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Analytics Dashboard</div>
            <div class="feature-description">
                Interactive visualizations, real-time metrics, and comprehensive threat intelligence reports.
            </div>
            <div style="margin-top: 1rem;">
                <span class="tech-badge">Real-time Charts</span>
                <span class="tech-badge">Export Reports</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Call to Action
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <div style="background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(6, 182, 212, 0.05)); border-radius: 24px; padding: 2rem; border: 1px solid rgba(79, 70, 229, 0.3);">
            <h3 style="color: #F1F5F9; margin-bottom: 1rem;">Ready to Secure Your Network?</h3>
            <p style="color: #94A3B8; margin-bottom: 1.5rem;">Upload a dataset and start detecting threats in real-time</p>
            <div style="display: flex; gap: 1rem; justify-content: center;">
                <div class="tech-badge" style="background: linear-gradient(135deg, #4F46E5, #06B6D4); color: white; border: none;">
                    🚀 Get Started
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == 'about':
    # About Page Content
    st.markdown("""
    <div class="hero-section animate">
        <div style="position: relative; z-index: 1;">
            <div class="big-title">
                📚 About IDS Guardian
            </div>
            <div class="subtitle">
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
        <div class="tech-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
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
                <div class="stats-badge">
                    <div class="stats-number">2.8M+</div>
                    <div class="stats-label">Network Flows</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; margin-top: 2rem; border-top: 1px solid rgba(79,70,229,0.2);">
    <p style="color: #64748B; font-size: 0.75rem;">
        🛡️ IDS Guardian Enterprise Platform | Powered by Mohammed Damlkhi
    </p>
    <p style="color: #4B5563; font-size: 0.7rem; margin-top: 0.5rem;">
        SOC-Ready | NIST Compliant | Enterprise Security Solution
    </p>
</div>
""", unsafe_allow_html=True)import streamlit as st
import time

st.set_page_config(
    page_title="AI Intrusion Detection System | Enterprise Security",
    page_icon="🛡️",
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
    .hero-section {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(6, 182, 212, 0.05));
        border-radius: 32px;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(79, 70, 229, 0.3);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
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
    
    .big-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #94A3B8;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }
    
    /* Feature Cards Premium */
    .feature-card-premium {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(10, 15, 46, 0.9));
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2rem;
        border: 1px solid rgba(79, 70, 229, 0.3);
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card-premium::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #4F46E5, #06B6D4);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .feature-card-premium:hover::before {
        transform: scaleX(1);
    }
    
    .feature-card-premium:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px -12px rgba(79, 70, 229, 0.4);
        border-color: rgba(79, 70, 229, 0.6);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #FFFFFF, #A5B4FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .feature-description {
        color: #94A3B8;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    /* Stats Section */
    .stats-section {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.05), rgba(6, 182, 212, 0.05));
        border-radius: 24px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(79, 70, 229, 0.2);
    }
    
    .stat-card {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: #94A3B8;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Technology Badges */
    .tech-badge {
        background: rgba(79, 70, 229, 0.1);
        border: 1px solid rgba(79, 70, 229, 0.3);
        border-radius: 12px;
        padding: 0.5rem 1rem;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.875rem;
        color: #A5B4FC;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(6, 182, 212, 0.05));
        border-left: 4px solid #4F46E5;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    /* ========== ENHANCED NAVIGATION BUTTONS ========== */
    .nav-button {
        width: 100%;
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(6, 182, 212, 0.05));
        border: 1px solid rgba(79, 70, 229, 0.3);
        border-radius: 14px;
        padding: 0.85rem 1rem;
        margin: 0.6rem 0;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .nav-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .nav-button:hover::before {
        left: 100%;
    }
    
    .nav-button:hover {
        transform: translateX(8px);
        border-color: #4F46E5;
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.2), rgba(6, 182, 212, 0.1));
        box-shadow: 0 5px 20px rgba(79, 70, 229, 0.3);
    }
    
    .nav-button-active {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.25), rgba(6, 182, 212, 0.15));
        border-left: 3px solid #4F46E5;
        border-color: #4F46E5;
        box-shadow: 0 5px 15px rgba(79, 70, 229, 0.2);
        transform: translateX(5px);
    }
    
    .nav-icon {
        font-size: 1.3rem;
        margin-right: 0.75rem;
        display: inline-block;
    }
    
    .nav-text {
        font-weight: 600;
        font-size: 1rem;
        letter-spacing: 0.3px;
    }
    
    .nav-badge {
        background: rgba(79, 70, 229, 0.3);
        border-radius: 20px;
        padding: 0.2rem 0.6rem;
        font-size: 0.7rem;
        margin-left: 0.5rem;
        color: #A5B4FC;
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
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10, 15, 46, 0.98), rgba(5, 7, 20, 0.98));
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(79, 70, 229, 0.2);
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
</style>
""", unsafe_allow_html=True)

# =============================
# NAVIGATION STATE
# =============================

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'app'

def navigate_to(page):
    st.session_state.page = page
    st.rerun()

# =============================
# SIDEBAR - ENHANCED NAVIGATION BUTTONS
# =============================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0 1rem 0;">
        <div style="font-size: 4rem; margin-bottom: 0.5rem;">🛡️</div>
        <h2 style="margin: 0; background: linear-gradient(135deg, #FFFFFF, #818CF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            IDS Guardian
        </h2>
        <p style="color: #64748B; font-size: 0.75rem; margin-top: 0.25rem;">Enterprise Security Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🚀 Navigation")
    
    # App Button (Home)
    if st.session_state.page == 'app':
        st.markdown("""
        <div class="nav-button nav-button-active">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center;">
                    <span class="nav-icon">🏠</span>
                    <span class="nav-text">Home</span>
                </div>
                <span class="nav-badge">Active</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            navigate_to('app')
    
    # About Button
    if st.session_state.page == 'about':
        st.markdown("""
        <div class="nav-button nav-button-active">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center;">
                    <span class="nav-icon">📚</span>
                    <span class="nav-text">About</span>
                </div>
                <span class="nav-badge">Active</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        if st.button("📚 About", key="nav_about", use_container_width=True):
            navigate_to('about')
    
   
    
    # System Status
    st.markdown("### 📊 System Status")
    st.markdown("""
    <div class="tech-badge" style="width: 100%; justify-content: center; margin: 0.5rem 0;">
        🟢 System Online
    </div>
    <div class="tech-badge" style="width: 100%; justify-content: center; margin: 0.5rem 0;">
        🤖 AI Active
    </div>
    <div class="tech-badge" style="width: 100%; justify-content: center; margin: 0.5rem 0;">
        🔒 Secure Connection
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Stats
    st.markdown("### 📈 Live Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Active Sessions", "1", delta="Online")
    with col2:
        st.metric("Threats Blocked", "0", delta="Monitoring")
    
    st.markdown("---")
    
    # Session Info
    st.markdown("### 👤 Session")
    st.info("**User:** Security Admin\n\n**Role:** Security Analyst\n\n**Last Active:** Just now")

# =============================
# MAIN CONTENT BASED ON NAVIGATION
# =============================

if st.session_state.page == 'app':
    # Hero Section
    st.markdown("""
    <div class="hero-section animate">
        <div style="position: relative; z-index: 1;">
            <div class="big-title">
                🛡️ AI Intrusion Detection System
            </div>
            <div class="subtitle">
                Advanced Machine Learning Cyber Security Platform
            </div>
            <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 1rem;">
                <span class="tech-badge">🤖 Machine Learning</span>
                <span class="tech-badge">⚡ Real-time Detection</span>
                <span class="tech-badge">📊 Advanced Analytics</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Description Section
    st.markdown("""
    <div class="info-box animate">
        <h3 style="color: #F1F5F9; margin-bottom: 1rem;">🔎 What This System Does</h3>
        <p style="color: #94A3B8; line-height: 1.6;">
            Analyze <strong style="color: #4F46E5;">network traffic datasets</strong> and detect cyber attacks 
            using <strong style="color: #06B6D4;">AI-powered machine learning models</strong> in real-time.
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1.5rem;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #10B981;">✓</span>
                <span style="color: #94A3B8;">Fast detection</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #10B981;">✓</span>
                <span style="color: #94A3B8;">High accuracy (98.7%)</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #10B981;">✓</span>
                <span style="color: #94A3B8;">Visual analytics dashboard</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="color: #10B981;">✓</span>
                <span style="color: #94A3B8;">Real-time monitoring</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats Section
    st.markdown("""
    <div class="stats-section animate">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">
            <div class="stat-card">
                <div class="stat-number">98.7%</div>
                <div class="stat-label">Detection Accuracy</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">&lt;100ms</div>
                <div class="stat-label">Response Time</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Continuous Monitoring</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">50+</div>
                <div class="stat-label">Attack Patterns</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Features Section
    st.markdown("<h2 style='text-align: center; margin: 2rem 0; color: #F1F5F9;'>✨ Key Features</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card-premium">
            <div class="feature-icon">📂</div>
            <div class="feature-title">Upload Dataset</div>
            <div class="feature-description">
                Easily upload CSV network traffic files for instant analysis. Supports multiple formats and large datasets.
            </div>
            <div style="margin-top: 1rem;">
                <span class="tech-badge">CSV Format</span>
                <span class="tech-badge">Batch Processing</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card-premium">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI Detection</div>
            <div class="feature-description">
                Advanced machine learning algorithms classify network traffic with high precision and minimal false positives.
            </div>
            <div style="margin-top: 1rem;">
                <span class="tech-badge">Random Forest</span>
                <span class="tech-badge">Deep Learning</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card-premium">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Analytics Dashboard</div>
            <div class="feature-description">
                Interactive visualizations, real-time metrics, and comprehensive threat intelligence reports.
            </div>
            <div style="margin-top: 1rem;">
                <span class="tech-badge">Real-time Charts</span>
                <span class="tech-badge">Export Reports</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Call to Action
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <div style="background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(6, 182, 212, 0.05)); border-radius: 24px; padding: 2rem; border: 1px solid rgba(79, 70, 229, 0.3);">
            <h3 style="color: #F1F5F9; margin-bottom: 1rem;">Ready to Secure Your Network?</h3>
            <p style="color: #94A3B8; margin-bottom: 1.5rem;">Upload a dataset and start detecting threats in real-time</p>
            <div style="display: flex; gap: 1rem; justify-content: center;">
                <div class="tech-badge" style="background: linear-gradient(135deg, #4F46E5, #06B6D4); color: white; border: none;">
                    🚀 Get Started
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == 'about':
    # About Page Content
    st.markdown("""
    <div class="hero-section animate">
        <div style="position: relative; z-index: 1;">
            <div class="big-title">
                📚 About IDS Guardian
            </div>
            <div class="subtitle">
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
        <div class="tech-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
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
                <div class="stats-badge">
                    <div class="stats-number">2.8M+</div>
                    <div class="stats-label">Network Flows</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; margin-top: 2rem; border-top: 1px solid rgba(79,70,229,0.2);">
    <p style="color: #64748B; font-size: 0.75rem;">
        🛡️ IDS Guardian Enterprise Platform | Powered by Mohammed Damlkhi
    </p>
    <p style="color: #4B5563; font-size: 0.7rem; margin-top: 0.5rem;">
        SOC-Ready | NIST Compliant | Enterprise Security Solution
    </p>
</div>
""", unsafe_allow_html=True)
