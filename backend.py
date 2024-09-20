import os
from dotenv import load_dotenv
from PyPDF2 import PdfFileReader
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

class DocumentProcessor:
    def __init__(self):
        self.documents = []
        self.vectorizer = TfidfVectorizer()
        self.doc_embeddings = None

    def process_pdf(self, file):
        pdf = PdfFileReader(file)
        text = ''
        for page in range(pdf.numPages):
            text += pdf.getPage(page).extract_text()
        self.documents.append(text)
        self._update_embeddings()

    def process_csv(self, file):
        df = pd.read_csv(file)
        text = ' '.join(df.astype(str).values.flatten())
        self.documents.append(text)
        self._update_embeddings()

    def process_text(self, file):
        with open(file, 'r') as f:
            text = f.read()
        self.documents.append(text)
        self._update_embeddings()

    def _update_embeddings(self):
        all_text = ' '.join(self.documents)
        self.doc_embeddings = self.vectorizer.fit_transform([all_text])

    def get_answer(self, query):
        query_vec = self.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.doc_embeddings)
        return similarity

def get_answer_from_docs(query):
    processor = DocumentProcessor()
    # Example code for processing PDFs, CSVs, and text files
    # processor.process_pdf(file) etc.
    # For demo purposes, we'll just simulate a response.
    return "Here's a simulated response based on your query."
