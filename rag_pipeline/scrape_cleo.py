import requests
from bs4 import BeautifulSoup
import json
import sys
import os
from tqdm import tqdm
from urllib.parse import urlparse

headers = {"User-Agent": "Mozilla/5.0"}

# Get topic URL from command-line
if len(sys.argv) < 2:
    print("Usage: python3 scrape_cleo.py <topic_url>")
    sys.exit(1)

START_URL = sys.argv[1]
BASE_URL = "https://stepstojustice.ca"

# Extract topic name from URL
topic_name = START_URL.strip("/").split("/")[-1]  # e.g., "family-law"

# Step 1: Load topic page
r = requests.get(START_URL, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

# Step 2: Extract Q&A links
qa_links = [
    a["href"] if a["href"].startswith("http") else BASE_URL + a["href"]
    for a in soup.select(f"a[href*='/questions/{topic_name}/']")
]

output = []

# Step 3: Visit each Q&A page
for url in tqdm(qa_links, desc="Scraping Q&A pages"):
    try:
        r2 = requests.get(url, headers=headers)
        r2.raise_for_status()
        soup2 = BeautifulSoup(r2.text, "html.parser")
    except Exception:
        continue

    title = soup2.find("h1").get_text(strip=True)
    main_div = soup2.find("div", class_="answer")
    if not main_div:
        continue

    paragraphs = [p.get_text(strip=True) for p in main_div.find_all("p")]
    content = "\n\n".join(paragraphs)

    output.append({
        "topic": topic_name,
        "url": url,
        "title": title,
        "content": content
    })

# Save to JSON with topic name
json_path = f"stepstojustice_{topic_name}.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✅ Saved {len(output)} Q&A documents to {json_path}")
