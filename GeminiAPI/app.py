from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
print("Gemini API Key:", api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Write a haiku about the beauty of nature."
)

# print(response.text)
st.title("Gemini API Response")
st.markdown(response.text)