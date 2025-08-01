import pickle
import faiss
import numpy as np
import json

# Load embeddings + chunks
with open("embeddings.pkl", "rb") as f:
    data = pickle.load(f)

embeddings = np.array(data["embeddings"]).astype("float32")
chunks = data["chunks"]

# Normalize for cosine similarity
faiss.normalize_L2(embeddings)

# Build FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatIP(dim)  # IP = inner product = cosine since normalized
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "faiss_index.index")

# Save metadata
with open("faiss_metadata.json", "w") as f:
    json.dump(chunks, f, indent=2)

print(f"✅ FAISS index saved with {index.ntotal} vectors.")
