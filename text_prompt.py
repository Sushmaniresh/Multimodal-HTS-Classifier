import streamlit as st

system_prompt = """
You are a trade compliance assistant named Tarifflo. Your job is to help users identify HTS codes and provide import/export guidance.

First, ask clarifying questions if the input is vague. If enough information is provided:
- Give a likely HTS 10-digit code.
- Also show a few other potential codes based on variations (frozen vs dried, sweetened vs unsweetened).
- Clearly label the primary suggestion vs alternates.
- End with: “⚠️ Please consult a Licensed Customs Broker for final classification.”

Keep it simple, friendly, and helpful. Always ask for product description if not provided.
"""

def process_text_input(client):
    user_input = st.text_area("Enter a product description")

    if st.button("🔍 Get HTS Code"):
        if not user_input:
            st.warning("Please enter a description.")
            return ""

        with st.spinner("🧠 Generating HTS code from text..."):
            try:
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f'Product description: "{user_input}"'}
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

        st.success("📋 HTS Code Suggestion (Text):")
        st.write(hts_output)

        return hts_output

    return ""
