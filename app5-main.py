import requests
from send_email import send_email


api_key = "230f1df4eb5343d2ad359f975f583dc7"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2024-06-27&sortBy=publishedAt&" \
      "apiKey=230f1df4eb5343d2ad359f975f583dc7"

# make a request
r = requests.get(url)

# get a dictionary with data
content = r.json()

body = " "
for article in content["articles"]:
    title = article.get("title", "No Title")
    description = article.get("description", "No Description")

    if title is None:
        title = "No Title"
    if description is None:
        description = "No Description"
    body += title + "\n" + description + "\n\n\n"

body = body.encode("utf-8")
send_email(message=body)
