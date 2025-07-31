# Legal Q&A Assistant with RAG (Retrieval-Augmented Generation)

This project implements a simple yet powerful **LLM-based legal question-answering assistant** using **retrieval-augmented generation (RAG)**. The system answers user questions using real-world legal documents (e.g., traffic accident FAQs, personal injury guidance) retrieved from a local vector store.

---

## 🔍 Objectives

This project was designed to:
- Demonstrate **RAG workflows** using vector search + LLM generation
- Work with **semi-structured legal documents**
- Showcase **prompt engineering** and **LLM integration**
- Prepare a **resume-ready, real-world AI use case** aligned with industry job roles (e.g., EvenUp)

---

## 🧩 Key Features

- ✅ Retrieval-augmented generation using **FAISS** + **LLM**
- ✅ Data ingestion pipeline for **scraped legal FAQs**
- ✅ Prompt templating for user questions
- ✅ Inference pipeline that returns generated answer + source context
- ✅ Ready to extend with FastAPI or LangChain

---

## 🏗 Tech Stack

- Python 3.10+
- `sentence-transformers` for embedding (e.g., `all-MiniLM-L6-v2`)
- `faiss-cpu` for similarity search
- OpenAI API or Hugging Face Transformers (`GPT2`, `T5`, `LLama2`, etc.)
- Jupyter notebook + optionally FastAPI

---

## 📁 Folder Structure

```
legal-qa-rag/
│
├── data/               # Raw and processed legal FAQs
├── rag_pipeline/       # Core code: ingest, embed, retrieve, generate
│   ├── embed.py
│   ├── retrieve.py
│   ├── generate.py
│   └── prompt_template.py
├── app.py              # Optional FastAPI server (in progress)
├── example_queries.ipynb
└── README.md
```

---

## ⚙️ Example Usage

```python
from rag_pipeline import retrieve, generate

question = "What should I do right after a car accident in Ontario?"
context_docs = retrieve(question)
answer = generate(question, context_docs)
print(answer)
```

---

## 📄 Example Sources

- [Ontario.ca Legal Aid and Traffic Collision Advice](https://www.ontario.ca/page/legal-aid)
- [Paralegal or Personal Injury Law Firm FAQs] (scraped, anonymized)

---

## 🧪 Future Additions

- A/B testing against other LLMs (e.g., T5 vs GPT2)
- FastAPI deployment
- LangChain-based document loading + retrieval
- RAG with ChromaDB or Pinecone

---

## 🤝 Credits

Created by [Niosha Hejazi](https://www.linkedin.com/in/nioshahejazi)  
Built as a portfolio project to demonstrate applied LLM development in the legal domain.
