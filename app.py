import os
from dotenv import load_dotenv
import streamlit as st
from openai import (
    APIConnectionError,
    APIError,
    AuthenticationError,
    BadRequestError,
    OpenAI,
    RateLimitError,
)

load_dotenv()

APP_TITLE = "My First LLM App"
MODEL_NAME = "gpt-5-nano"
SYSTEM_PROMPT_PATH = "prompts/system_prompt.txt"
DEFAULT_SYSTEM_PROMPT = "You are a helpful beginner-friendly AI assistant."

ASSISTANT_MODES = {
    "General Assistant": "Give practical, concise help in plain language.",
    "Interview Coach": "Explain your thinking clearly and include short examples.",
    "Code Explainer": "Break down code step by step for a beginner.",
}

EXAMPLE_PROMPTS = {
    "Summarize a concept": "Explain what a Python virtual environment is in simple terms.",
    "Learn by steps": "Teach me how an API request works, step by step.",
    "Code explanation": "Explain this line: response = client.responses.create(...)",
}


def load_system_prompt():
    if not os.path.exists(SYSTEM_PROMPT_PATH):
        return DEFAULT_SYSTEM_PROMPT

    try:
        with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as file:
            prompt = file.read().strip()
            return prompt or DEFAULT_SYSTEM_PROMPT
    except OSError:
        # Fallback keeps the app usable even if file permissions/path are broken.
        return DEFAULT_SYSTEM_PROMPT


def build_system_prompt(base_prompt, selected_mode):
    mode_instruction = ASSISTANT_MODES[selected_mode]
    return f"{base_prompt}\n\nMode instruction: {mode_instruction}"


def get_response(client, system_prompt, user_prompt):
    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.output_text


def main():
    api_key = os.getenv("OPENAI_API_KEY")

    st.set_page_config(page_title=APP_TITLE)
    st.title(APP_TITLE)

    default_system_prompt = load_system_prompt()

    assistant_mode = st.selectbox("Assistant Mode", list(ASSISTANT_MODES.keys()))

    selected_example = st.selectbox(
        "Quick Example Prompt (optional)",
        ["None"] + list(EXAMPLE_PROMPTS.keys()),
    )
    if st.button("Use Example Prompt") and selected_example != "None":
        st.session_state["user_prompt"] = EXAMPLE_PROMPTS[selected_example]

    system_prompt = st.text_area(
        "System Prompt", value=default_system_prompt, height=180
    )
    user_prompt = st.text_area(
        "User Prompt", placeholder="Ask me anything...", key="user_prompt"
    )

    if st.button("Run", type="primary"):
        if not api_key:
            st.error(
                "Missing OPENAI_API_KEY. Add it to your .env file and restart Streamlit."
            )
            return

        if not user_prompt.strip():
            st.warning("Please enter a user prompt before running.")
            return

        final_system_prompt = build_system_prompt(system_prompt, assistant_mode)

        try:
            client = OpenAI(api_key=api_key)
            with st.spinner("Thinking..."):
                answer = get_response(client, final_system_prompt, user_prompt)

            st.subheader("Response")
            st.write(answer)

        except AuthenticationError:
            st.error("Authentication failed. Check your OPENAI_API_KEY and try again.")
        except RateLimitError:
            st.error("Rate limit hit. Wait a moment and try again.")
        except APIConnectionError:
            st.error("Could not connect to OpenAI. Check your internet connection.")
        except BadRequestError as err:
            st.error(f"Request error: {err}")
        except APIError as err:
            st.error(f"OpenAI API error: {err}")
        except Exception as err:
            st.error(f"Unexpected error: {err}")


if __name__ == "__main__":
    main()
