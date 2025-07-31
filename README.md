# Legal Q&A Assistant with RAG (Retrieval-Augmented Generation)

This is a work-in-progress implementation of a **legal-domain question-answering system** using **retrieval-augmented generation (RAG)**. The goal is to build a prototype that answers user questions using legal FAQs retrieved from a local vector store and enhanced with LLM-based responses.

---

## 🔍 Project Goal

This project aims to:

- Explore **RAG-style workflows** combining vector retrieval + LLM generation
- Work with **semi-structured legal text**, such as traffic accident FAQs
- Practice **prompt engineering** and **context-aware inference**
- Serve as a portfolio project aligned with real-world NLP/ML engineering roles

---

## 🧩 Planned Features

- Document ingestion and preprocessing for legal FAQ content  
- Sentence embedding and similarity search using **FAISS**  
- Prompt formatting and question-handling logic  
- LLM generation based on retrieved context  
- Optional: FastAPI-based backend or notebook interface

---

## 🏗 Tech Stack (Planned)

- Python 3.10+  
- `sentence-transformers` for embeddings  
- `faiss-cpu` for vector indexing  
- `transformers` from Hugging Face  
- OpenAI API (optional), or local LLM (T5, GPT2)  
- Jupyter Notebook or FastAPI interface

---

## 📄 Example Use Case

> “What should I do immediately after a car accident in Ontario?”

The system will retrieve matching answers from a small scraped set of traffic accident FAQs and generate a natural language answer using an LLM.

---

## 📁 Project Structure (planned)

```
legal-qa-rag/
├── data/                  # Raw and cleaned FAQs
├── rag_pipeline/          # Code modules for embedding, search, and generation
├── example_queries.ipynb  # Notebook interface
└── README.md
```

---

## 📌 Current Status

🔧 Currently building:  
- Data ingestion and embedding pipeline  
- Retrieval + generation logic

Coming next:  
- Notebook interface  
- Evaluation examples and FastAPI wrapper

---

## 🤝 Credits

Created by [Niosha Hejazi](https://www.linkedin.com/in/nioshahejazi)  
This project is part of my portfolio to demonstrate applied LLM development and RAG workflows for real-world use cases.
