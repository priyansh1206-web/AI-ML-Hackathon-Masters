import numpy as np
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

# load dataset
with open("clean_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# chunk text
chunk_size = 500
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# create vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(chunks).toarray()

# create FAISS index
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(vectors).astype("float32"))

# ask user question
query = input("Ask a question about the course: ")

query_vector = vectorizer.transform([query]).toarray()

# search similar chunks
D, I = index.search(np.array(query_vector).astype("float32"), k=2)

print("\nMost relevant information:\n")

for i in I[0]:
    print(chunks[i])
    print("\n---\n")