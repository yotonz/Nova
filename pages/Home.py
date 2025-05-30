# pages/Home.py

import streamlit as st

# Wrapper function for routing

def app():
    # Hero Section
    st.markdown("""
        <div style='text-align: center; padding-top: 2rem;'>
            <p class='hero-text'>🚀 Welcome to NOVA Studio (MVP)</p>
            <p class='sub-text'>Create enterprise-grade, AI-powered assistants in minutes.</p>
        </div>
    """, unsafe_allow_html=True)

    # CTA Button
    st.markdown("""
        <div style='text-align: center; margin-top: 2rem;'>
            <a href='/CreateAssistant' target='_self'>
                <button class='cta-button'>✨ Create Your Own AI Assistant Now</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")

    # Highlights
    col1, col2, col3 = st.columns(3)
    col1.success("""
    👥 **For Teams**
    Internal support for IT, HR, Admin, and more.
    """)
    col2.info("""
    🔐 **Secure by Design**
    Hosted on Microsoft Azure with enterprise-grade compliance.
    """)
    col3.warning("""
    🤖 **Smart & Proactive**
    Understands context. Responds like a human.
    """)

    st.write("---")

    # Why Nova Section
    st.markdown("""
    ### 🌟 Why Choose NOVA?
    - 🏢 Centralized support across departments
    - 💡 Tailored to your company and team needs
    - ✨ Powered by the latest Azure OpenAI models
    - 🌐 Integrates with your tools (SharePoint, PRTG, Teams, etc.)
    """)

    st.toast("Explore more via the sidebar ←", icon="📖")
