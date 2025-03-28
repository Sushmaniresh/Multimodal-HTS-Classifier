from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import streamlit as st

@st.cache_resource
def load_blip_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

# Tarifflo prompt
system_prompt = """
You are a trade compliance assistant named Tarifflo. Your job is to help users identify HTS codes and provide import/export guidance.

First, ask clarifying questions if the input is vague. If enough information is provided:
- Give a likely HTS 10-digit code.
- Also show a few other potential codes based on variations (frozen vs dried, sweetened vs unsweetened).
- Clearly label the primary suggestion vs alternates.
- End with: “⚠️ Please consult a Licensed Customs Broker for final classification.”

Keep it simple, friendly, and helpful. Always ask for product description if not provided.
"""

def process_image_input(uploaded_file, client):
    if not uploaded_file:
        return ""

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", width=300)

    processor, model = load_blip_model()

    # Step 1: Generate caption
    with st.spinner("🔍 Generating image description..."):
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        base_caption = processor.decode(out[0], skip_special_tokens=True)

    st.info("📝 BLIP Base Caption:")
    st.write(base_caption)

    # Step 2: Enhance caption
    with st.spinner("✨ Enhancing product description..."):
        enhancement_prompt = f"""
Expand the following product description to include:
- Material
- Primary use or function
- Size, packaging, or any helpful trade details

Description: "{base_caption}"
"""
        try:
            enhanced = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": enhancement_prompt}],
                temperature=0.4,
                max_tokens=150
            )
            enhanced_desc = enhanced.choices[0].message.content
        except Exception as e:
            enhanced_desc = f"❌ Error enhancing description: {e}"

    st.success("🔎 Enhanced Product Description:")
    st.write(enhanced_desc)

    # Step 3: HTS Classification
    with st.spinner("📦 Predicting HTS code..."):
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f'Product description: "{enhanced_desc}"'}
            ]
            response = client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                temperature=0.5,
                max_tokens=250
            )
            hts_output = response.choices[0].message.content
        except Exception as e:
            hts_output = f"❌ Error generating HTS code: {e}"

    st.success("📋 HTS Code Suggestion (Image):")
    st.write(hts_output)

    return hts_output
