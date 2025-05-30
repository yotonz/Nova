# pages/AboutUs.py

import streamlit as st

# Wrapper for routed execution
def app():
    st.title("👨‍💼 About Us")

    st.markdown("""
    ### Welcome to **Nova Studio**

    At Nova Studio, we believe in democratizing AI for teams of all sizes. Our goal is to help you build human-like AI assistants tailored to your business needs in minutes.

    Our mission is to bridge the gap between complex AI technologies and everyday business operations by making powerful assistants accessible, secure, and customizable.

    **What we value:**
    - 🤝 Collaboration
    - 🔐 Security and privacy
    - ⚡ Innovation with simplicity
    - 🌍 Real-world impact

    Nova Studio was designed with enterprise standards in mind, while maintaining startup agility. We are committed to continually evolving with your needs.

    ---
    Want to collaborate or contribute? Reach out via our Contact page!
    """)

# Optional standalone test run
def main():
    app()

if __name__ == "__main__":
    main()
