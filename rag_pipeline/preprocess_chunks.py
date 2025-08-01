import json
import nltk
import os
from nltk.tokenize import sent_tokenize
import spacy
nlp = spacy.load("en_core_web_sm")



MAX_TOKENS = 250

def split_into_chunks(text, max_tokens=200):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]
    
    chunks = []
    current_chunk = ""
    current_tokens = 0
    
    for sentence in sentences:
        token_count = len(sentence.split())
        if current_tokens + token_count > max_tokens:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
            current_tokens = token_count
        else:
            current_chunk += " " + sentence
            current_tokens += token_count

    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

# Load raw Q&A JSON
with open("stepstojustice_family.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_chunks = []

for qa in data:
    chunks = split_into_chunks(qa["content"])
    for i, chunk in enumerate(chunks):
        all_chunks.append({
            "topic": qa["topic"],
            "url": qa["url"],
            "title": qa["title"],
            "chunk_id": f"{qa['url']}#chunk{i}",
            "text": chunk
        })

print(f"Generated {len(all_chunks)} total chunks.")

# Save to new file
with open("processed_chunks.json", "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, ensure_ascii=False, indent=2)

