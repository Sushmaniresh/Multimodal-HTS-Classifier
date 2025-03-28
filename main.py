import streamlit as st
st.set_page_config(page_title="Multimodal HTS Classifier", page_icon="📦")

from dotenv import load_dotenv
import os
from openai import OpenAI
from image_prompt import process_image_input
from text_prompt import process_text_input

# Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("❌ OPENAI_API_KEY not found.")
    st.stop()

client = OpenAI(api_key=api_key)

# App UI
st.title("📦 Multimodal HTS Classifier – Tarifflo Demo Project")
# 🔗 Add this line right here
st.sidebar.markdown("🔗 [Visit Official HTS Search Site](https://hts.usitc.gov)", unsafe_allow_html=True)


st.write("Choose to upload an image or enter a product description to get HTS code predictions.")

# Tabs
tab1, tab2 = st.tabs(["🖼️ Image Input", "✍️ Text Input"])

with tab1:
    uploaded_image = st.file_uploader("Upload product image", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        process_image_input(uploaded_image, client)

with tab2:
    process_text_input(client)
