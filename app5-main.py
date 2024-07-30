import requests
from send_email import send_email

topic = ["tesla"]
api_key = "230f1df4eb5343d2ad359f975f583dc7"
url = f"https://newsapi.org/v2/everything?q={topic}" \
      "&from=2024-06-29&sortBy=publishedAt&" \
      "apiKey=230f1df4eb5343d2ad359f975f583dc7&language=en"

# make a request
r = requests.get(url)

# get a dictionary with data
content = r.json()

body = " "
for article in content["articles"][:10]:
    title = article.get("title", "No Title")
    description = article.get("description", "No Description")

    if title is None:
        title = "No Title"
    if description is None:
        description = "No Description"
    body += "Subject: Today's News" + "\n" + title + "\n" + description + "\n" + article["url"] + "\n\n\n"

body = body.encode("utf-8")
send_email(message=body)
