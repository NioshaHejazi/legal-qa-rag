# Legal Q&A Assistant using Retrieval-Augmented Generation (RAG)

This project is a fully functional prototype of a legal-domain question-answering system built using retrieval-augmented generation (RAG) and large language models (LLMs). It combines dense vector retrieval using FAISS with context-aware answer generation via OpenAI's GPT-4, allowing the system to produce accurate and grounded responses to legal questions. All responses are based on public legal FAQs, making the assistant reliable, transparent, and aligned with real-world legal information.


## 🔍 Project Purpose

- Answer user legal questions using real legal resources (e.g., CLEO, StepsToJustice)
- Demonstrate a practical RAG workflow applied to semi-structured legal text
- Showcase NLP techniques like vector search, prompt engineering, and GPT-4 generation
- Provide a reproducible, portfolio-grade legal tech pipeline



## 🛠 Technologies Used

- **Python 3.10+**
- **FAISS** – Fast Approximate Nearest Neighbor Search
- **SentenceTransformers** – (e.g., `all-MiniLM-L6-v2`) for dense embeddings
- **OpenAI GPT-4 API** – for answer generation
-  Streamlit for deployment/demo



## 🚀 How to Use

The project includes an interactive interface (`app.py`) where users can:

- Select a legal topic from a dropdown menu (e.g., housing law, language rights)
- Enter a natural language question
- Receive a GPT-4 generated answer grounded in retrieved legal content


### 🔧 Backend Pipeline

The full RAG workflow is automatically triggered through the interface or can be run step-by-step using scripts:

1. Run `scrape_and_process.py` to fetch, clean, and chunk public legal FAQs  
2. Use `embed_chunks.py` to generate vector embeddings  
3. Build a FAISS index using `build_faiss_index.py`  
4. Query the index using `query_faiss.py`  
5. Generate GPT-4 responses using `generate_answer.py`

All components are modular and can be reused or extended independently. The UI (`app.py`) ties everything into a seamless legal Q&A experience.

## 🤝 Credits

Created by [Niosha Hejazi](https://www.linkedin.com/in/nioshahejazi)  
This project demonstrates applied NLP, LLMs, and vector search for real-world legal question answering.
