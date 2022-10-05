import requests

url = "http://localhost:9200/products"

payload = ""
headers = {}

# 스키마를 확인하는 요청
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
