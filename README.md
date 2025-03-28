# 📦 Multimodal HTS Classifier – Demo

An AI-powered trade classification tool that helps identify accurate **10-digit HTS codes** (Harmonized Tariff Schedule) using either a **product image** or a **text description**.

This demo combines **BLIP (image captioning)** and **OpenAI GPT-4** to generate enhanced product descriptions and provide HTS code suggestions based on international trade classification logic.

---

## 🔍 What It Does

- 🖼️ **Image Input**: Upload a product image → AI generates a description → Enhances it for trade context → Suggests HTS code(s)
- ✍️ **Text Input**: Manually enter a product description → Get HTS code predictions
- 📋 Includes enhanced product descriptions for clarity
- 🔗 Direct links to [HTS Search Portal](https://hts.usitc.gov)

---

## 🚀 Live App (Coming Soon)

> Deployed version will be accessible via Streamlit Cloud

---

## 🛠️ Tech Stack

- 🤖 [OpenAI GPT-4](https://platform.openai.com)
- 📸 [BLIP Image Captioning](https://huggingface.co/Salesforce/blip-image-captioning-base)
- ⚙️ [Streamlit](https://streamlit.io)
- 🐍 Python 3.9+

---

## 💻 Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/hts-classifier-demo.git
cd hts-classifier-demo

2. **Install dependencies**
pip install -r requirements.txt

3. **create .env*
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

4. **Run the app*
streamlit run main.py
