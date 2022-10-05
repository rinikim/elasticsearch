import requests

url = "http://localhost:9200/products/_search"

payload = {}
headers = {}

# 인덱스 확인 요청
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
