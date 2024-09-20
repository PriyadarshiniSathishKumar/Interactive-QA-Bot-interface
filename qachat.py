from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found. Please check your environment variables.")
    st.stop()
    
genai.configure(api_key=api_key)

# Initialize the model and chat
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    """Function to get a response from the Gemini model."""
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo", layout="wide")

st.header("Gemini Q&A Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input
input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and input_text:
    with st.spinner("Generating response..."):
        response = get_gemini_response(input_text)
        # Add user query and response to session state chat history
        st.session_state['chat_history'].append(("You", input_text))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))
else:
    st.warning("Please enter a question before submitting.")

# Display chat history
st.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
