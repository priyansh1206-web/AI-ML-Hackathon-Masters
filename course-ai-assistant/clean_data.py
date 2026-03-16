import re

with open("course_data.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

text = re.sub(r'\s+', ' ', text)
text = re.sub(r'[^\x00-\x7F]+', ' ', text)

with open("clean_data.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaning finished!")