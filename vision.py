from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found. Please check your environment variables.")
    st.stop()
    
genai.configure(api_key=api_key)

def get_gemini_response(text, image):
    """Function to get a response from the Gemini model based on text and image."""
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        if text:
            response = model.generate_content([text, image])
        else:
            response = model.generate_content(image)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, there was an error processing your request."

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo", layout="wide")

st.header("Gemini Image Analysis Application")

# User input
input_text = st.text_input("Input Prompt:", key="input")

# File uploader for images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Submit button
if st.button("Tell me about the image"):
    if uploaded_file:
        with st.spinner("Generating response..."):
            response = get_gemini_response(input_text, image)
            st.subheader("The Response is")
            st.write(response)
    else:
        st.warning("Please upload an image before submitting.")

