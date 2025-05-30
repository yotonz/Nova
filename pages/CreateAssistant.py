# pages/CreateAssistant.py

import streamlit as st
from utils.file_upload import extract_text_from_file, chunk_text

# Wrapper function for routing
def app():
    st.title("🤖 Create Your AI Assistant")
    st.markdown("Build your assistant in just a few steps. Your data is safe and nothing is sent to external servers.")

    st.write("## Step 1: Choose Skills")
    selected_skills = st.multiselect("Select one or more skills", ["HR", "IT"])

    st.write("## Step 2: Select Tone")
    tone = st.radio("Choose the assistant's tone", ["Formal", "Friendly"], horizontal=True)

    st.write("## Step 3: Upload Knowledge Base Files")
    uploaded_files = st.file_uploader("Upload PDFs, DOCX or TXT files", accept_multiple_files=True)
    context_chunks = []
    if uploaded_files:
        for file in uploaded_files:
            raw_text = extract_text_from_file(file)
            chunks = chunk_text(raw_text)
            context_chunks.extend(chunks)

    st.write("## Step 4: Assistant Details")
    col1, col2 = st.columns(2)
    with col1:
        assistant_name = st.text_input("Assistant Name", placeholder="E.g. NovaBot")
    with col2:
        company_name = st.text_input("Company Name", placeholder="E.g. Bounteous")

    additional_instructions = st.text_area("Any additional features, personality, or skills?", height=100)

    st.write("## Step 5: Select AI Model")
    model = st.selectbox("Choose a model", ["GPT-4o", "GPT-3.5 Turbo"])

    st.write("---")
    if st.button("💬 Test Your Assistant"):
        st.session_state.config = {
            "skills": selected_skills,
            "tone": tone,
            "assistant_name": assistant_name,
            "company_name": company_name,
            "instructions": additional_instructions,
            "model": model,
            "context_chunks": context_chunks
        }
        st.switch_page("pages/ChatAssistant.py")

    st.write("---")
    st.info("🔐 All uploaded files are kept secure within Azure Storage and processed within your enterprise boundary.")
    st.warning("⚠️ No sensitive data is sent to external servers. Everything is processed locally within your environment.")

if __name__ == "__main__":
    app()
