import os
import pickle
from openai import OpenAI

# Load your API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load the question and top chunks
with open("retrieved_chunks.pkl", "rb") as f:
    question, chunks = pickle.load(f)

# Build prompt from chunks
context = "\n\n".join([chunk["text"] for chunk in chunks])
prompt = f"""You are a helpful legal assistant specialized in Ontario family law.

Answer this legal question using only the information below.

Context:
{context}

Question:
{question}

Answer:"""

# Generate answer using GPT-4o (better than 3.5)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful legal assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3
)

# Print the final result
print("\n🤖 Answer:\n")
print(response.choices[0].message.content.strip())
