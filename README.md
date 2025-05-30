# 🧠 Nova Studio (MVP)

Nova Studio is a fully customizable AI assistant builder. Upload knowledge bases, choose a tone and model, and chat instantly — all within a polished, secure, and beautiful Streamlit app.

---

## 🚀 Features

* 🎨 Interactive UI with sidebar navigation and modern styling
* 🛠️ Create custom AI assistants with:

  * Name, tone (Formal / Friendly), and skill (IT / HR)
  * Upload of PDF, DOCX, TXT knowledge bases
  * Support for GPT-4o and GPT-3.5 Turbo via Azure OpenAI
* 💬 Chat interface that responds with context-aware, natural answers
* 🔒 All data stays local — no external API calls beyond Azure OpenAI / Search

---

## 📁 Project Structure

```
nova_studio/
├── main.py                   # 🧠 Main entry point (use instead of app.py)
├── .env                      # 🔐 Azure OpenAI and Search configuration
├── requirements.txt          # 📦 Python dependencies
├── assets/
│   └── style.css             # 🎨 Global styling for app
├── components/
│   ├── nav.py                # 🔀 Custom sidebar
│   └── prompt_builder.py     # 🧩 Builds dynamic prompts
├── data/
│   └── sample_kb/            # 📚 Placeholder for test KBs
├── pages/
│   ├── Home.py
│   ├── CreateAssistant.py
│   ├── ChatAssistant.py
│   ├── AboutUs.py
│   ├── ContactUs.py
│   ├── InfoSec.py
│   └── HowItWorks.py
├── utils/
│   ├── auth.py               # (optional - not implemented yet)
│   ├── azure_openai.py       # 🤖 GPT interaction
│   ├── file_upload.py        # 📄 Reads PDF, DOCX, TXT
│   └── vector_store.py       # 🔍 Azure Search context retriever
```

---

## ⚙️ Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/yotonz/nova_studio.git
cd nova_studio
pip install -r requirements.txt
```

### 2. Configure `.env`

Create a `.env` file in the root directory:

```
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_KEY=...
AZURE_SEARCH_ENDPOINT=...
AZURE_SEARCH_KEY=...
AZURE_SEARCH_INDEX=...
AZURE_OPENAI_DEPLOYMENT_GPT4=gpt-4
```

### 3. Run the App

```bash
streamlit run main.py
```

---

## 📸 Screenshot

![nova](https://lottie.host/6e68aeb9-19dc-40e7-98c6-2e7d346efb85/ZFSorTxYt1.json)

---

## 💡 Ideas to Extend

* Add user authentication
* Export assistant configs to JSON
* Deploy with Streamlit Community Cloud or Azure App Service

---

## 🏁 Built for Hackathons

This MVP was crafted for rapid prototyping and impressing judges with real-time, smart interactions.

> Designed to feel professional, powerful, and magical ✨
