"""
Ingest Knowledge Pipeline
Collects, validates, and indexes all documents from knowledge/*/*.json
Generates:
1. data/knowledge_corpus.json (canonical structured dataset with rich metadata)
2. data/bm25_index.json (lexical BM25 inverted index and vocabulary)
3. rag-knowledge.json (portfolio client-side corpus)
"""

import json
import os
import re
import math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

STOPWORDS = {
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', 'as', 'at',
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'cannot', 'could',
    'did', 'do', 'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have',
    'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is',
    'it', 'its', 'itself', 'let', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once',
    'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'she', 'should', 'so',
    'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they',
    'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when',
    'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'would', 'you', 'your', 'yours', 'yourself', 'yourselves'
}

def tokenize(text: str):
    if not text:
        return []
    clean = re.sub(r'[^a-zA-Z0-9\s]', ' ', text.lower())
    return [w for w in clean.split() if len(w) > 1 and w not in STOPWORDS]

def main():
    documents = []
    categories = os.listdir(KNOWLEDGE_DIR)
    
    for cat in sorted(categories):
        cat_dir = os.path.join(KNOWLEDGE_DIR, cat)
        if not os.path.isdir(cat_dir):
            continue
        for fname in sorted(os.listdir(cat_dir)):
            if fname.endswith(".json"):
                fpath = os.path.join(cat_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    doc = json.load(f)
                    
                    # Validate required schema
                    required_fields = ["id", "type", "name", "category", "technologies", "source", "tags", "content"]
                    for field in required_fields:
                        if field not in doc:
                            raise ValueError(f"Document {fpath} missing required field: {field}")
                    
                    documents.append(doc)
    
    print(f"Loaded and validated {len(documents)} structured documents from {len(categories)} categories.")
    
    # 1. Save canonical corpus
    corpus_file = os.path.join(DATA_DIR, "knowledge_corpus.json")
    with open(corpus_file, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)
    print(f"Saved canonical corpus to {corpus_file}")

    # 2. Build BM25 index & statistics
    doc_tokens = []
    doc_lens = []
    df = {}
    
    for doc in documents:
        # Full searchable representation combines title, category, technologies, tags, and content
        search_str = f"{doc['name']} {doc['category']} {' '.join(doc['technologies'])} {' '.join(doc['tags'])} {doc.get('stats', '')} {doc['content']}"
        tokens = tokenize(search_str)
        doc_tokens.append(tokens)
        doc_lens.append(len(tokens))
        
        unique_tokens = set(tokens)
        for term in unique_tokens:
            df[term] = df.get(term, 0) + 1

    N = len(documents)
    avg_dl = sum(doc_lens) / (N or 1)
    
    idf = {}
    for term, freq in df.items():
        # Standard Lucene / BM25 IDF formula
        idf[term] = math.log(1.0 + (N - freq + 0.5) / (freq + 0.5))

    bm25_data = {
        "num_docs": N,
        "avg_doc_len": avg_dl,
        "vocab_size": len(df),
        "idf": idf,
        "doc_lengths": doc_lens
    }
    
    bm25_file = os.path.join(DATA_DIR, "bm25_index.json")
    with open(bm25_file, "w", encoding="utf-8") as f:
        json.dump(bm25_data, f, indent=2)
    print(f"Saved BM25 index (vocab: {len(df)} terms) to {bm25_file}")

    # 3. Synchronize rag-knowledge.json for client-side frontend
    client_corpus = []
    for doc in documents:
        client_corpus.append({
            "id": doc["id"],
            "title": doc["name"],
            "category": doc["category"],
            "tags": doc["tags"],
            "content": doc["content"],
            "stats": doc.get("stats", ""),
            "slug": doc.get("slug", ""),
            "type": doc["type"],
            "technologies": doc["technologies"],
            "source": doc["source"],
            "github_url": doc.get("github_url", ""),
            "demo_url": doc.get("demo_url", "")
        })

    client_file = os.path.join(BASE_DIR, "rag-knowledge.json")
    with open(client_file, "w", encoding="utf-8") as f:
        json.dump(client_corpus, f, indent=2)
    print(f"Synchronized client-side knowledge base to {client_file}")

if __name__ == "__main__":
    main()
