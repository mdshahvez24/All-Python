import requests

#get request

response = requests.get("https://www.codewithharry.com")
print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"

data = { 
    "title": "foo",
    "body": 'bar',
    "userId": 1,
}

response = requests.post(url, json=data)

print(response.text)