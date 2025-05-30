# pages/ChatAssistant.py

import streamlit as st
from components.prompt_builder import build_prompt
from utils.vector_store import search_documents
from utils.azure_openai import ask_openai

# Wrapper function for routing
def app():
    st.set_page_config(page_title="Chat with Assistant", layout="wide")
    st.title("🤖 Chat with Your Assistant")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Get assistant configurations
    config = st.session_state.get("config", {})
    assistant_name = config.get("assistant_name", "Nova")
    company_name = config.get("company_name", "Your Company")
    selected_skill = config.get("skills", ["IT"])[0] if config.get("skills") else "IT"
    selected_tone = config.get("tone", "Formal")
    selected_model = config.get("model", "gpt-4")
    context_chunks = config.get("context_chunks", [])

    # Input from user
    user_input = st.chat_input("Ask something...")

    if user_input:
        with st.spinner("Thinking..."):
            # Optional: augment context via vector search
            vector_context = search_documents(user_input)
            full_context = context_chunks + vector_context
            prompt = build_prompt(user_input, full_context, assistant_name, company_name, selected_skill, selected_tone)
            response = ask_openai(prompt, model=selected_model)

            # Save conversation
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("assistant", response))

    # Display full history
    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(message)

if __name__ == "__main__":
    app()
