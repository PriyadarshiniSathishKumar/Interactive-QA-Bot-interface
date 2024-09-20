# Use Python slim image to reduce size
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt

# Upgrade pip and install the dependencies with retries and timeout settings
RUN pip install --upgrade pip && \
    pip install --default-timeout=100 --retries 5 -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables for dotenv (if needed)
ENV PYTHONUNBUFFERED=1

# Expose the port that Streamlit runs on
EXPOSE 8501

# Command to run the application (adjust this based on your app entry point)
CMD ["streamlit", "run", "app.py"]
