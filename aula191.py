# requests para requisições HTTP
import requests

# Portas em que rodam
# http:// -> 80
# http:// -> 443
url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)