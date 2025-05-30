# main.py (formerly app.py)

import streamlit as st
from components.nav import render_sidebar
import os

# ✅ Set global config before any Streamlit code
st.set_page_config(
    page_title="NOVA Studio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ Apply global CSS
style_path = os.path.join("assets", "style.css")
if os.path.exists(style_path):
    with open(style_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🔧 Hide Streamlit's default sidebar pages
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] ul {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Load custom sidebar navigation
route = render_sidebar()

# ✅ Dynamic route import based on selection
if route == "Home":
    import pages.Home as current_page
elif route == "Create Assistant":
    import pages.CreateAssistant as current_page
elif route == "Chat Assistant":
    import pages.ChatAssistant as current_page
elif route == "About Us":
    import pages.AboutUs as current_page
elif route == "Contact Us":
    import pages.ContactUs as current_page
elif route == "InfoSec":
    import pages.InfoSec as current_page
elif route == "How it Works":
    import pages.HowItWorks as current_page
else:
    st.error("🚨 Page not found. Check your navigation.")
    st.stop()

# ✅ Call the wrapped app() from selected module
if hasattr(current_page, "app"):
    current_page.app()
else:
    st.warning("Page missing an 'app()' method. Please define one.")
