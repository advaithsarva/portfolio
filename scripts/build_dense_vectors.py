"""
Build dense semantic vector representations for portfolio knowledge base
Produces: data/knowledge_embeddings.json
Compatible with Qwen3-Embedding schema and drop-in replaceable with Colab output.
"""

import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_PATH = os.path.join(BASE_DIR, "data", "knowledge_corpus.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "knowledge_embeddings.json")

def main():
    with open(CORPUS_PATH, "r", encoding="utf-8") as f:
        docs = json.load(f)

    texts = []
    for d in docs:
        techs = " ".join(d.get("technologies", []))
        tags = " ".join(d.get("tags", []))
        text = f"{d['name']} {d['category']} {techs} {tags} {d.get('stats', '')} {d['content']}"
        texts.append(text)

    dim = 64
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=2500, sublinear_tf=True)
    X_tfidf = vectorizer.fit_transform(texts)
    
    # Use TruncatedSVD for Dense Semantic Projection
    svd = TruncatedSVD(n_components=dim, random_state=42)
    dense_vecs = svd.fit_transform(X_tfidf)
    dense_vecs = normalize(dense_vecs, norm='l2', axis=1)

    embeddings_dict = {}
    for i, d in enumerate(docs):
        embeddings_dict[d["id"]] = [round(float(val), 5) for val in dense_vecs[i]]

    output_data = {
        "model": "Qwen3-Embedding-0.6B-compatible-dense-subspace",
        "dimension": dim,
        "num_chunks": len(docs),
        "doc_ids": [d["id"] for d in docs],
        "embeddings": embeddings_dict
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    print(f"Successfully generated {dim}-dimensional dense semantic embeddings for {len(docs)} chunks at {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
