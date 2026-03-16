import requests
from bs4 import BeautifulSoup

url = "https://www.coursera.org/learn/ai-for-everyone"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()

with open("course_data.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Scraping complete!")