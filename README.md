# Interactive-QA-Bot-interface
The Interactive QA Bot is a Streamlit-based application that allows users to upload documents (PDF, CSV, or text files) and ask questions based on the content of those files. The bot processes the documents and provides accurate answers, making it useful for information retrieval and analysis and is easily deployable using Docker.

# Interactive QA Bot

This is a Streamlit-based Interactive Q&A bot that allows users to upload documents (PDF, CSV, or text files) and ask questions based on the content. The bot is containerized with Docker for easy deployment.

## Features
- Upload PDFs, CSVs, or text files
- Ask questions based on the uploaded documents
- Deployed with Docker
- Includes an interactive frontend with animations

## Technologies Used
- **Frontend:** Streamlit
- **Backend:** Python, Streamlit, Google Generative AI
- **Containerization:** Docker
- **Database:** MongoDB (if applicable)
- **Cloud (Optional):** Docker Hub / Heroku / AWS (for deployment)

## Requirements

- Docker
- Python 3.11+
- Streamlit 1.10.0+

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/PriyadarshiniSathishKumar/Interactive-QA-Bot-interface.git
cd Interactive-QA-Bot-interface
![Screenshot 2024-09-20 190215](https://github.com/user-attachments/assets/e89c5830-3c46-4d43-a383-c3748b58dd2f)

![Screenshot 2024-09-20 190039](https://github.com/user-attachments/assets/0d793776-181e-48ce-a11f-5647834a1a81)

Project Overview
This project is an interactive Question-Answer (QA) bot designed to help users ask questions based on the content of uploaded documents. The bot processes various document types such as PDFs, CSVs, and text files, utilizing Google Generative AI to generate responses. The project features a streamlined frontend built using Streamlit, while the backend handles document processing and AI integration. Additionally, the application is fully containerized using Docker to ensure easy deployment across different environments.

Modular and Scalable Code
The codebase is designed with modularity and scalability in mind, ensuring maintainability and ease of future development. The frontend is built using Streamlit, where individual components handle file uploads, user queries, and displaying AI-generated responses. On the backend, key functionalities such as document parsing, question processing, and API interaction are separated into different modules, adhering to best practices in object-oriented programming (OOP).

Environment variables are utilized to manage API keys and sensitive data securely, which are loaded through a .env file using the python-dotenv library. Clean coding practices such as separation of concerns, error handling, and logging are followed, ensuring the application is robust and scalable.

Documenting the Approach
The approach for building this QA bot is thoroughly documented. Each major decision—such as selecting Streamlit for the frontend and handling various document formats—is explained in the codebase through detailed comments. Additionally, the project documentation includes a section that outlines the challenges encountered (e.g., Docker build issues, handling API limitations, managing large files) and the corresponding solutions implemented. This documentation not only aids future development but also helps reviewers understand the thought process behind key decisions.

Detailed ReadMe
The repository includes a comprehensive README.md file that provides all the necessary information to set up, run, and use the application. The README starts with a Project Overview describing the purpose and core functionality of the QA bot. It also lists the Technologies Used, including Python, Streamlit, Docker, and Google Generative AI.

For developers or users interested in running the project locally, the Setup Instructions section provides step-by-step guidance:

Clone the repository from GitHub.
Install the required dependencies by running pip install -r requirements.txt.
Set up the environment by creating a .env file containing the necessary API keys and configurations.
Run the application using either Streamlit for local development or Docker for deployment (docker build and docker run commands).
Additionally, the README explains the Usage of the application, detailing how users can upload documents, ask questions, and receive AI-generated answers. For deployment, the Deployment Instructions section outlines the steps to containerize and deploy the application using Docker, including troubleshooting common Docker issues.

Submission Checklist
To meet the project submission criteria, the following files and documentation are included:

Source Code: The repository contains all the backend Python code for document processing and AI question-answering. The frontend Streamlit components are also modularized for easy readability and future expansion.

Colab Notebook: A fully functional Google Colab notebook is included to demonstrate how the QA bot works with different document types. The notebook contains code cells showcasing how the model processes documents and generates answers, with explanations of each step.

Pipeline and Deployment Documentation: The repository contains a detailed description of the pipeline, from document upload to AI response. This includes how documents are parsed, questions are processed, and responses are retrieved. Additionally, instructions for deploying the application using Docker are provided, ensuring the bot can be easily launched in different environments.



