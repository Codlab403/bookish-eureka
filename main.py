import streamlit as st  # type: ignore
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv  # type: ignore
import os

# Print environment details for debugging
print("ENV path:", os.getcwd())
print("Files in folder:", os.listdir())

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Configure Gemini
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-2.0-flash")  # Updated model name
except Exception as e:
    raise RuntimeError(f"Failed to configure Generative AI: {e}")

# List available models
try:
    models = genai.list_models()
    print("Available models:")
    for model in models:
        print(f"Model: {model}")  # Adjust this based on the structure of the object
except Exception as e:
    print(f"Failed to list models: {e}")

#
# Streamlit app configuration
st.set_page_config(page_title="Socratic AI Tutor")
st.title("Socratic AI Tutor")
st.markdown(
    """
    Ask your question or start a topic of study. The AI will guide you through Socratic questioning to help you discover answers yourself.
    """
)

# Initialize session state
if "convo" not in st.session_state:
    st.session_state["convo"] = None

# User input
user_input = st.text_input("Enter your question or topic:", "What is gravity?")

if st.button("Start Tutoring Session") and user_input:
    with st.spinner("Thinking like Socrates..."):
        try:
            convo = model.start_chat(history=[])
            convo.send_message(
                f"Act as a Socratic tutor. Guide the user in understanding this concept: '{user_input}' through question-based dialogue."
            )

            response = convo.last.text
            st.markdown("**Socratic Tutor:**")
            st.markdown(response)

            st.session_state["convo"] = convo
        except Exception as e:
            st.error(f"An error occurred: {e}")

if st.session_state["convo"]:
    followup = st.text_input("Your response:")
    if st.button("Continue") and followup:
        with st.spinner("Continuing Socratic dialogue..."):
            try:
                convo = st.session_state["convo"]
                convo.send_message(followup)
                response = convo.last.text
                st.markdown("**Socratic Tutor:**")
                st.markdown(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Add footer
st.markdown("---")
st.markdown("Created with :sparkles: using Gemini and Streamlit.")
