import streamlit as st

st.set_page_config(page_title="My First LLM App")

st.title("My First LLM App")

system_prompt = st.text_area(
    "System Prompt", value="You are a helpful beginner-friendly AI assistant."
)

user_prompt = st.text_area("User Prompt")

if st.button("Run"):
    st.subheader("Prompt Preview")
    st.write("### System")
    st.write(system_prompt)
    st.write("### User")
    st.write(user_prompt)

    st.subheader("Placeholder Response")
    st.write("Your model output will go here later.")
