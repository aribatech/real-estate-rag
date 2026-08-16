# Real Estate RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for answering real estate property questions using **Python, LangChain, Gemini, FAISS, and Streamlit**.

## Features

* Supports PDF, CSV, and XLSX documents
* PDF, CSV, and XLSX loaders
* Recursive text splitting
* Gemini embedding model
* FAISS vector database
* Similarity-based retrieval
* Gemini LLM for generating answers
* Simple Streamlit chatbot interface

## RAG Architecture

```text
Documents
    ↓
Loaders
    ↓
Splitter
    ↓
Embeddings
    ↓
FAISS Vector Database
    ↓
Similarity Search
    ↓
Relevant Context
    ↓
Gemini LLM
    ↓
Final Answer
```

## Tech Stack

**Python • LangChain • Google Gemini • FAISS • Pandas • PyPDF • OpenPyXL • Streamlit**

## Run Locally

Install dependencies:

```bash
uv sync
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

Run the application:

```bash
uv run --active streamlit run app.py
```

The application will be available at `http://localhost:8501`.

## Learning Objectives

This project covers **RAG architecture, document loaders, text splitters, embeddings, vector databases, retrieval, LLM generation, and Streamlit deployment**.

