with open("clean_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i+chunk_size])

print("Total chunks:", len(chunks))

for i in range(min(3, len(chunks))):
    print("\nChunk", i+1)
    print(chunks[i])