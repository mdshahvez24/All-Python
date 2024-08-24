import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}tesla&from=2023-12-29&sortBy=publishedAt&apiKey=574fda027b0c49e389c7fa8128a753d4"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
  

# GET
# https://newsapi.org/v2/everything?q=apple&from=2024-01-28&to=2024-01-28&sortBy=popularity&apiKey=API_KEY


# https://newsapi.org/v2/everything?q=tesla&from=2023-12-29&sortBy=publishedAt&apiKey=API_KEY



# # 574fda027b0c49e389c7fa8128a753d4
# _forward
# GET
# https://newsapi.org/v2/everything?q=tesla&from=2023-12-29&sortBy=publishedAt&apiKey=574fda027b0c49e389c7fa8128a753d4