# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download necessary NLTK data
RUN python -m nltk.downloader punkt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable to run Streamlit
ENV STREAMLIT_SERVER_PORT=8501

# Run app.py when the container launches
CMD ["streamlit", "run", "app/main.py"]