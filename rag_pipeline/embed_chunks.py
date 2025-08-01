import json
import pickle
from sentence_transformers import SentenceTransformer

# Load chunked data
with open("processed_chunks.json", "r") as f:
    chunks = json.load(f)

texts = [chunk["text"] for chunk in chunks]

# Load the embedding model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
print(f"Embedding {len(texts)} chunks...")
embeddings = model.encode(texts, show_progress_bar=True)

# Save both embeddings and chunks
with open("embeddings.pkl", "wb") as f:
    pickle.dump({
        "embeddings": embeddings,
        "texts": texts,       # needed by query_faiss.py
        "chunks": chunks      # full metadata
    }, f)

print(f"✅ Done! Saved {len(embeddings)} embeddings to embeddings.pkl")
