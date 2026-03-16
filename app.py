import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="My First LLM App")
st.title("My First LLM App")

system_prompt = st.text_area(
    "System Prompt", value="You are a helpful beginner-friendly AI assistant."
)

user_prompt = st.text_area("User Prompt")

if st.button("Run"):
    if not api_key:
        st.error("Missing OPENAI_API_KEY in your .env file.")
    elif not user_prompt.strip():
        st.warning("Please enter a user prompt.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            response = client.responses.create(
                model="gpt-5-nano",
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            )

            st.subheader("Response")
            st.write(response.output_text)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
