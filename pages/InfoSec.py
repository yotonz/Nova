# pages/InfoSec.py

import streamlit as st

# Wrapper for routed execution
def app():
    st.title("🔐 Information Security")

    st.markdown("""
    At **Nova Studio**, your data privacy and security are our top priorities. We are committed to ensuring enterprise-grade protection at every layer.

    ### 🔒 Key InfoSec Practices:

    - **Azure Infrastructure:** Hosted on Microsoft Azure with region-specific compliance and SLAs.
    - **Data Isolation:** Each tenant’s knowledge base and chat history are isolated and never shared.
    - **No Data Leakage:** Uploaded files and user inputs are never transmitted to third-party APIs.
    - **Encryption:** All communications are encrypted in transit (TLS) and at rest.
    - **Access Control:** Role-based access for admins and users to restrict actions.
    - **Audit Trails:** All access and activity logs are monitored and retained.

    ### 📜 Compliance Goals:

    We aim to align with:
    - SOC 2 Type II
    - GDPR
    - ISO/IEC 27001
    - HIPAA (for healthcare use cases)

    > Security is not a feature — it's a foundation.

    Please contact us for detailed architecture or policy documentation.
    """)

# Optional standalone test run
def main():
    app()

if __name__ == "__main__":
    main()
