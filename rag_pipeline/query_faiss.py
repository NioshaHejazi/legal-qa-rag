import pickle
import faiss
from sentence_transformers import SentenceTransformer
import pickle
import numpy as np

# Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("faiss_index.index")

# Load metadata (text chunks)
with open("embeddings.pkl", "rb") as f:
    data = pickle.load(f)
    texts = [chunk["text"] for chunk in data["chunks"]]
    metas = data["chunks"]


# --- Ask a user question ---
question = input("Enter your legal question:\n> ")

# Embed the question
query_vec = model.encode([question])

# Search FAISS
top_k = 3
D, I = index.search(np.array(query_vec).astype("float32"), top_k)

# Print results
print("\n🔍 Top Matches:\n")
for idx in I[0]:
    print(f"→ Title: {metas[idx]['title']}")
    print(f"URL: {metas[idx]['url']}")
    print(f"Content: {texts[idx][:500]}...\n")
top_chunks = [metas[idx] for idx in I[0]]

with open("retrieved_chunks.pkl", "wb") as f:
    pickle.dump((question, top_chunks), f)
