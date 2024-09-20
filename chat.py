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
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    """Function to get a response from Gemini model."""
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo", layout="wide")

st.header("Gemini Q&A Application")

# User input
input_text = st.text_input("Ask a question:", key="input")

# Submit button
if st.button("Ask the question"):
    if input_text:
        with st.spinner("Generating response..."):
            response = get_gemini_response(input_text)
            st.subheader("The Response is")
            
            # Display the response chunks
            for chunk in response:
                st.write(chunk.text)  # Display each chunk of response

            # Display chat history
            st.subheader("Chat History:")
            st.write(chat.history)
    else:
        st.warning("Please enter a question before submitting.")
