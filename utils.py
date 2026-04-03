"""Shared utilities for the IDS Guardian Streamlit application.

This module centralises CSS styles, application-wide constants, and helper
functions that are reused across multiple pages.  Import the helpers here
rather than duplicating boilerplate in every page file.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Risk-level thresholds for the attack-rate percentage metric
# ---------------------------------------------------------------------------

#: Advertised detection accuracy of the deployed model (displayed in the UI).
MODEL_ACCURACY: str = "99.7%"

#: Attack rate at or above this value is considered *critical*.
ATTACK_RATE_CRITICAL: int = 50

#: Attack rate at or above this value is considered *high* risk.
ATTACK_RATE_HIGH: int = 30

#: Attack rate at or above this value is considered *moderate* risk.
ATTACK_RATE_MODERATE: int = 10

# ---------------------------------------------------------------------------
# Base CSS injected into every page
# ---------------------------------------------------------------------------

_BASE_CSS: str = """
<style>
    /* ── Google Fonts ─────────────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ── Global reset ─────────────────────────────────────────────────── */
    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* ── App background ───────────────────────────────────────────────── */
    .stApp {
        background: linear-gradient(135deg, #0A0F2E 0%, #070B1A 100%);
    }

    /* ── Sidebar ──────────────────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(10, 15, 46, 0.98), rgba(5, 7, 20, 0.98));
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(79, 70, 229, 0.2);
    }

    /* ── Primary action button ────────────────────────────────────────── */
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

    /* ── Custom scrollbar ─────────────────────────────────────────────── */
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

    /* ── Fade-in entrance animation ───────────────────────────────────── */
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

    /* ── Highlighted informational box ───────────────────────────────── */
    .info-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(6, 182, 212, 0.05));
        border-left: 4px solid #4F46E5;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
</style>
"""


def inject_base_css() -> None:
    """Inject the shared base CSS styles into the current Streamlit page.

    Call this once at the top of each page file, immediately after
    ``st.set_page_config``, to apply the application-wide theme.
    """
    st.markdown(_BASE_CSS, unsafe_allow_html=True)


def render_footer(version: str = "2.0.0") -> None:
    """Render the standard application footer.

    Args:
        version: Application version string displayed in the footer text.
    """
    st.markdown(
        f"""
        <div style="text-align: center; padding: 2rem; margin-top: 2rem;
                    border-top: 1px solid rgba(79, 70, 229, 0.2);">
            <p style="color: #64748B; font-size: 0.75rem;">
                🛡️ IDS Guardian v{version} | Enterprise Security Platform
                | {MODEL_ACCURACY} Detection Accuracy
            </p>
            <p style="color: #4B5563; font-size: 0.7rem; margin-top: 0.5rem;">
                SOC-Ready | NIST Compliant | Enterprise Security Solution
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
