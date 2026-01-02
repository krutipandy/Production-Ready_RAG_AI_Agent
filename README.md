🚀 Overview
This application allows users to upload PDF documents and chat with them using an LLM. It transforms static documents into a searchable vector database, enabling the AI to provide accurate, context-aware answers based specifically on the uploaded content.

Key Features
PDF Ingestion: Automatic chunking and embedding of PDF documents using LlamaIndex.

Vector Search: High-performance similarity search powered by a local Qdrant instance.

Production Orchestration: Workflow management, retries, and deep observability via Inngest.

Interactive UI: A clean, user-friendly interface built with Streamlit.

AI Inference: Optimized prompt engineering using OpenAI's GPT-4o-mini.

🛠️ Tech Stack
Language: Python

Orchestration: Inngest (for workflow management and reliability)

Vector Database: Qdrant (running via Docker)

Frameworks: FastAPI (Backend) & Streamlit (Frontend)

AI Tools: LlamaIndex (Data Loading) & OpenAI (Embeddings/LLM)

📋 Prerequisites
Python 3.10+

Docker Desktop (to run the Qdrant database)

Node.js (to run the Inngest Dev Server)

OpenAI API Key

⚙️ Installation & Setup
Clone the repository:

Bash

git clone <your-repo-url>
cd rag-production-app
Install dependencies: This project uses uv for fast dependency management.

Bash

uv init .
uv add fastapi inngest llama-index-core llama-index-readers-file python-dotenv qdrant-client uvicorn streamlit openai
Environment Variables: Create a .env file in the root directory:

Code snippet

OPENAI_API_KEY=your_sk_key_here
Start Qdrant (Vector DB):

Bash

docker run -d --name qdrant -p 6333:6333 -v $(pwd)/qdrant_storage:/qdrant/storage qdrant/qdrant
🏃 Running the Application
To run the full production environment, you need to start three separate services:

Start the FastAPI Backend:

Bash

uv run uvicorn main:app --reload
Start the Inngest Dev Server:

Bash

npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest
Start the Streamlit Frontend:

Bash

uv run streamlit run streamlit_app.py
🧠 How it Works
Trigger: A user uploads a PDF via Streamlit, which sends a rag/ingest.pdf event to Inngest.

Step 1 (Load): Inngest triggers the load_and_chunk step, using LlamaIndex to split the PDF into manageable text segments [38:12].

Step 2 (Upsert): Segments are converted into vectors via OpenAI's embedding model and stored in Qdrant [51:58].

Query: When a user asks a question, the application embeds the query, searches Qdrant for the top 5 most relevant segments, and passes them to GPT-4o-mini for a concise answer [01:00:46].

📚 Reference & Credits
This project is based on the comprehensive tutorial by Tech With Tim.

Video Title: How to Build a Production-Ready RAG AI Agent in Python (Step-by-Step)

Channel: Tech With Tim

Original Source: YouTube Link
