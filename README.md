# Streamlit + OpenAI Chatbot

A beginner-friendly chatbot project built with Streamlit and the OpenAI API. It is intentionally small, readable, and easy to explain in an interview.

![App Screenshot](assets/app-screenshot.png)

> Screenshot placement recommendation: keep this image directly under the project title/summary so recruiters and reviewers see the UI immediately.

## Why This Project
- Shows end-to-end API integration in a real UI
- Demonstrates prompt control through editable system prompts
- Includes basic product thinking with assistant modes
- Handles common API failures with clear user-facing errors

## Features
- Clean Streamlit interface
- Assistant mode dropdown with 3 modes:
  - General Assistant
  - Interview Coach
  - Code Explainer
- Editable system prompt loaded from `prompts/system_prompt.txt`
- OpenAI Responses API call using `gpt-5-nano`
- Friendly error handling for missing keys, rate limits, network issues, and bad requests

## Project Structure
```text
.
├── app.py
├── requirements.txt
├── prompts/
│   └── system_prompt.txt
└── README.md
```

## Quick Start
1. Clone this repository.
2. Create and activate a virtual environment.
3. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
4. Create a `.env` file in the root folder:
	```env
	OPENAI_API_KEY=your_api_key_here
	```
5. Run the app:
	```bash
	streamlit run app.py
	```

## How It Works
1. Load environment variables and optional base system prompt.
2. Let the user choose an assistant mode from a dropdown.
3. Combine base prompt + mode instruction.
4. Send user input to the OpenAI API.
5. Display the model response or a helpful error message.

## Interview Talking Points
- Why a small app first: easier debugging, faster iteration, clearer explanation.
- How prompt design changes behavior without changing model code.
- How specific error messages improve user experience.
- How to keep code modular without introducing heavy architecture.

## Next Improvements (Still Simple)
- Add chat history in session state
- Add model selection dropdown
- Add basic input/output logging for debugging

