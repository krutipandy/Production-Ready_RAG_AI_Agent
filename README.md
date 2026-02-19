
# 🚀 Production-Ready RAG AI Agent

**A robust, production-grade Retrieval-Augmented Generation (RAG) application built with Python.**
This project goes beyond simple RAG demos—featuring key production-level engineering capabilities like observability, logging, retries, rate limiting, and orchestration. 

# 🧠 Why This Project Matters

Most RAG examples are simple scripts or notebooks. This repository is built *from the ground up* as a **deployable RAG service** with real-world concerns addressed:

✔️ **Observability** — Logs, performance metrics, and debug-friendly outputs.
✔️ **Rate Limiting** — Protects APIs and resource usage.
✔️ **Retries & Resilience** — Robust handling of flaky external APIs.
✔️ **Orchestration** with Inngest — Modern serverless workflow handling.
✔️ **Vector Database Integration** — Efficient semantic search over ingested data.
✔️ **Interactive UI** — Streamlit front end for easy exploration.

# 💡 Project Highlights

## 🛠️ Production-Grade Features

* **Inngest orchestration** for reliable, asynchronous task pipelines
* **Observability & Logging** built-in for debugging and monitoring
* **Retry Policies** with exponential backoff on transient failures
* **Rate Limits** to guard against abuse and overuse
* **Vector search** for fast, semantic retrieval
* **Fully modular architecture** so each component can be swapped or enhanced


# 📦 Tech Stack

| Layer                 | Technology                  |
| --------------------- | --------------------------- |
| Backend               | Python                      |
| Workflow Orchestrator | Inngest                     |
| Vector DB             | (configured in project)     |
| UI                    | Streamlit                   |
| Logging               | Standardized Python logging |
| Deployment            | Ready for Docker / Cloud    |


# 🧱 Project Structure

```plainte
├── main.py                # CLI entrypoint
├── streamlit_app.py       # Frontend
├── data_loader.py         # Data ingestion
├── vector_db.py           # Vector store setup
├── custom_types.py        # Data models & types
├── uv.lock                # Dependency lock
├── pyproject.toml         # Project config
├── .python-version        # Python version pin
├── README.md              # This file
└── assets/                # Diagrams and illustrations
```

# 🚀 Quickstart

1. Install

```bash
git clone https://github.com/krutipandy/Production-Ready_RAG_AI_Agent.git
cd Production-Ready_RAG_AI_Agent
pip install -r requirements.txt
```

2. Configure

Create a `.env` with API keys and DB configs:

```
OPENAI_API_KEY=your_key_here
VECTOR_DB_URL=...
```

3. Run Local Dev

Backend

```bash
python main.py
```

Frontend

```bash
streamlit run streamlit_app.py
```

4. Production Deployment

* Containerize with Docker
* Deploy to cloud providers (AWS, GCP, etc.)
* Add observability stack (Prometheus, Grafana)


# 🧪 Built-In Tests

```bash
pytest
```

Automated tests ensure:

* Vector retrieval correctness
* Workflow orchestration
* API endpoint responses



