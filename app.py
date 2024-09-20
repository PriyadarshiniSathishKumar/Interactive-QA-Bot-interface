import streamlit as st
from backend import DocumentProcessor

# Initialize document processor
processor = DocumentProcessor()

def display_gif():
    """Display loading GIF animation"""
    st.markdown(
        """
        <style>
        .loading-gif {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }
        </style>
        <img src="data:image/gif;base64,{base64_encoded_gif}" class="loading-gif">
        """.format(base64_encoded_gif=base64.b64encode(open('images/loading.gif', 'rb').read()).decode()),
        unsafe_allow_html=True
    )

st.set_page_config(page_title="Interactive QA Bot", layout="wide")

st.title("Interactive Q&A Bot")

# File uploader for documents
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "csv", "txt"])
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        processor.process_pdf(uploaded_file)
    elif uploaded_file.type == "text/csv":
        processor.process_csv(uploaded_file)
    elif uploaded_file.type == "text/plain":
        processor.process_text(uploaded_file)
    st.success("Document processed successfully!")

input_query = st.text_input("Ask a question based on the uploaded document:")

if st.button("Submit"):
    with st.spinner("Generating response..."):
        response = processor.get_answer(input_query)
        st.subheader("The Response is")
        st.write(response)
