# pages/HowItWorks.py

import streamlit as st

# Wrapper for routed execution
def app():
    st.title("⚙️ How It Works")

    st.markdown("""
    Nova Studio simplifies the process of building AI assistants for your organization.

    ### 🛠 Step-by-Step Breakdown:

    1. **Skill Selection**  
       Choose one or more core skills such as HR or IT to define your assistant’s purpose.

    2. **Tone & Personality**  
       Select whether your assistant should speak formally or casually — or add custom behaviors.

    3. **Knowledge Base Upload**  
       Upload PDFs, DOCX, or TXT files that contain the internal knowledge your assistant should learn from.

    4. **Assistant Setup**  
       Provide your company name, bot name, and any additional requirements.

    5. **Model Selection**  
       Choose between cutting-edge models like GPT-4o or GPT-3.5 Turbo.

    6. **Instant Testing**  
       Chat with your assistant instantly to validate its responses and capabilities.

    ---

    ### 🤖 Behind the Scenes:

    - Uses **Azure Cognitive Search** to retrieve relevant context from your KB
    - Constructs a **dynamic prompt** tailored to your configuration
    - Generates responses using **Azure OpenAI GPT deployments**

    Nova Studio handles the complexity — you focus on results.
    """)

# Optional standalone test run
def main():
    app()

if __name__ == "__main__":
    main()
