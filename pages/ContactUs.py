# pages/ContactUs.py

import streamlit as st

# Wrapper for routed execution
def app():
    st.title("📬 Contact Us")

    st.markdown("""
    If you have any questions, suggestions, or want to collaborate — feel free to reach out!
    
    We're always excited to connect with innovators, developers, and enterprises exploring the future of AI.
    """)

    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name")
        with col2:
            email = st.text_input("Your Email")

        message = st.text_area("Your Message", height=150)
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email and message:
                st.success("✅ Thank you! We'll get back to you shortly.")
            else:
                st.error("❌ Please fill in all fields before submitting.")

    st.markdown("---")
    st.info("You can also contact us directly at: support@novastudio.ai")

# Optional standalone test run
def main():
    app()

if __name__ == "__main__":
    main()
