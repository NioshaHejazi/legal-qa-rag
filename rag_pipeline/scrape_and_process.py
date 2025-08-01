import sys
import os
import subprocess
import json

if len(sys.argv) < 2:
    print("Usage: python3 scrape_and_process.py <topic_url>")
    sys.exit(1)

# Get topic URL from command-line
url = sys.argv[1]
topic_name = url.strip("/").split("/")[-1]  # e.g., "family-law"

print(f"🔍 Processing topic: {topic_name}")

# Step 1: Scrape
print("📥 Step 1: Scraping legal content...")
scrape_result = subprocess.run(["python3", "scrape_cleo.py", url])
if scrape_result.returncode != 0:
    print("❌ Scraping failed.")
    sys.exit(1)

# Step 2: Preprocess chunks
print("✂️ Step 2: Preprocessing chunks...")
with open(f"stepstojustice_{topic_name}.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

chunks = []
from spacy.lang.en import English
nlp = English()
sentencizer = nlp.add_pipe("sentencizer")

chunk_size = 200
for item in raw_data:
    doc = nlp(item["content"])
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

    for i in range(0, len(sentences), 8):
        chunk = " ".join(sentences[i:i+8])
        chunks.append({
            "text": chunk,
            "title": item["title"],
            "url": item["url"],
            "topic": topic_name
        })

with open("chunked_qa_data.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)
print(f"✅ Chunked {len(chunks)} pieces.")

# Step 3: Embed
print("🔗 Step 3: Embedding chunks...")
subprocess.run(["python3", "embed_chunks.py"])

# Step 4: Build FAISS index
print("📦 Step 4: Building FAISS index...")
subprocess.run(["python3", "build_faiss_index.py"])

print("🎉 Done! You can now ask questions in Streamlit.")
