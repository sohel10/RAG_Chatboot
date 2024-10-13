# RAG App Demo

This repository contains a **Retrieval-Augmented Generation (RAG)** application built using **Streamlit** and **Langchain**. The app allows users to ask questions related to documents retrieved from specified URLs. It integrates OpenAI's GPT models for answering queries based on retrieved documents.

## Overview

The **RAG App** retrieves documents from a list of URLs, splits them into chunks, and processes user queries using OpenAI’s GPT. The application provides context-based answers by searching the retrieved documents and generating responses using a language model.

## Features

- **Document Retrieval**: Loads content from specified URLs.
- **Question Answering**: Users can ask questions about the content of the retrieved documents.
- **Similarity Search**: Uses similarity search to retrieve relevant document chunks based on the user’s query.
- **OpenAI Integration**: Leverages OpenAI's GPT model for generating answers.
- **Streamlit Interface**: Provides a user-friendly, chat-like interface to input queries and view answers.

## Prerequisites

- **Python 3.7+**
- **Pip**
- **OpenAI API Key**
- **Git**

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-repo/rag-app-demo.git
    cd rag-app-demo
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv rag_env
    source rag_env/bin/activate  # For Windows: `rag_env\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up OpenAI API key**:

    Create a `.env` file and add your OpenAI API key:

    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Usage

1. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

2. **Open the app**:

   After running the command above, the app will be accessible at `http://localhost:8501` on your local machine.

### How It Works

- **Document Loading**: The app retrieves content from a predefined list of URLs related to Michigan Value Collaborative (MVC).
- **Query Input**: Users can ask questions such as "What is Michigan Value Care?".
- **Answer Generation**: The app uses a combination of document similarity retrieval and the OpenAI GPT model to generate accurate answers based on the retrieved documents.

## Project Structure

```bash
.
├── app.py                  # Main application script
├── .env                    # Environment variables (API key)
├── requirements.txt        # Python dependencies
├── chroma_db/              # Directory to store Chroma vector database
└── README.md               # This readme file
