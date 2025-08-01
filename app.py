import streamlit as st
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import os
import subprocess

# --- Config ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("Missing OpenAI API key. Please set OPENAI_API_KEY as environment variable.")
    st.stop()

client = OpenAI(api_key=OPENAI_API_KEY)
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

st.title("📚 Ontario Legal Assistant (All Topics)")
st.write("Select a legal topic and ask your question.")

# --- Legal Topic Selector ---
topics = {
    "Family Law": "https://stepstojustice.ca/legal-topic/family-law/",
    "Housing Law": "https://stepstojustice.ca/legal-topic/housing-law/",
    "Employment and Work": "https://stepstojustice.ca/legal-topic/employment-and-work/",
    "Criminal Law": "https://stepstojustice.ca/legal-topic/criminal-law/",
    "Income Assistance": "https://stepstojustice.ca/legal-topic/income-assistance/",
    "Abuse and Family Violence": "https://stepstojustice.ca/legal-topic/abuse-and-family-violence/",
    "Tribunals and Courts": "https://stepstojustice.ca/legal-topic/tribunals-and-courts/",
    "Wills and Powers of Attorney": "https://stepstojustice.ca/legal-topic/wills-and-powers-of-attorney/",
    "Debt and Consumer Rights": "https://stepstojustice.ca/legal-topic/debt-and-consumer-rights/",
    "Human Rights": "https://stepstojustice.ca/legal-topic/human-rights/",
    "Education Law": "https://stepstojustice.ca/legal-topic/education/",
    "Provincial Offences": "https://stepstojustice.ca/legal-topic/provincial-offences/",
    "Immigration Law": "https://stepstojustice.ca/legal-topic/immigration/",
    "Refugee Law": "https://stepstojustice.ca/legal-topic/refugee-law/",
    "Health and Disability": "https://stepstojustice.ca/legal-topic/health-and-disability/",
    "French Language Rights": "https://stepstojustice.ca/legal-topic/french-language-rights/",
    "Help from Lawyers and Paralegals": "https://stepstojustice.ca/legal-topic/help-lawyers-and-paralegals/"
}

selected_topic = st.selectbox("Choose a legal topic:", list(topics.keys()))
topic_url = topics[selected_topic]

if st.button("Scrape and Process Selected Topic"):
    with st.spinner("Scraping and processing topic..."):
        result = subprocess.run(["python3", "scrape_and_process.py", topic_url], capture_output=True, text=True)
        st.code(result.stdout)
        if result.returncode != 0:
            st.error("❌ There was a problem during scraping or processing.")
        else:
            st.success("✅ Topic processed successfully!")

st.markdown("---")
question = st.text_input("Enter your legal question:", placeholder="e.g., How can I get a divorce certificate in Ontario?")

if st.button("Get Answer") and question:
    try:
        with open("embeddings.pkl", "rb") as f:
            data = pickle.load(f)
            texts = [chunk["text"] for chunk in data["chunks"]]
            metas = data["chunks"]
        index = faiss.read_index("faiss_index.index")
    except Exception as e:
        st.error("❌ Embedding index or data not found. Please scrape a topic first.")
        st.stop()

    with st.spinner("Thinking..."):
        query_vec = model.encode([question])
        D, I = index.search(np.array(query_vec).astype("float32"), 3)
        top_chunks = [metas[i] for i in I[0]]
        context = "\n\n".join([chunk["text"] for chunk in top_chunks])
        prompt = f"Answer the following legal question using the information below.\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:"

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful legal assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        answer = response.choices[0].message.content
        st.markdown("### 🤖 Answer:")
        st.write(answer)

        with st.expander("📄 Sources"):
            for i, chunk in enumerate(top_chunks):
                st.markdown(f"**{i+1}. [{chunk['title']}]({chunk['url']})**\n\n{chunk['text'][:400]}...")
