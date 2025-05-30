# utils/azure_openai.py

from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def ask_openai(prompt, model=None):
    model = model or os.getenv("AZURE_OPENAI_DEPLOYMENT_GPT4", "gpt-4")

    system_message = (
        "You are a highly intelligent, emotionally aware AI assistant. You respond in a clear, human-like, and engaging manner. "
        "Use company context and assistant identity when appropriate. Keep answers helpful and empathetic, always avoiding robotic tone."
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1200,
        presence_penalty=0.3,
        frequency_penalty=0.1
    )

    return response.choices[0].message.content
