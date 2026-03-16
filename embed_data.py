import numpy as np
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

# read data
with open("clean_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# chunk text
chunk_size = 500
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

print("Total chunks:", len(chunks))

# convert to vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(chunks).toarray()

# create FAISS index
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(vectors).astype("float32"))

print("Vector DB created with", index.ntotal, "vectors")