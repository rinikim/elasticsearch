import requests
import json

# products라는 인덱스 생성
url = "http://localhost:9200/products"

# payload는 아래 request에 data body로 들어가게 된다.
payload = json.dumps({
    "settings": {
        "index": {
            # 분산을 하지 않고 모든 인덱스를 하나의 샤드에 저장 (100으로 지정해주면 색인이 100개로 나누어지게 됩니다.)
            "number_of_shards": 1,
			# "number_of_shards": 100, "number_of_replicas": 10으로 지정하게 되면 100개의 샤드들이 모두 replication을 10개씩 가지게 되는 것을 의미한다.
			# 그래서 총 1,000개의 서빙 인덱스가 생기게 되는 것을 의미한다.
			# replica는 availability를 위해서 존재하고, shard는 performance를 위해 존재한다. (더 빨리 병행하도록 load를 균형을 맞추기 위해서 존재한다.)
            "number_of_replicas": 1
        },
        "analysis": {
            "analyzer": {
                "analyzer-name": {
                    "type": "custom",
					# token을 keyword 방식으로 맞춘다.
                    "tokenizer": "keyword",
                    "filter": "lowercase"
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "id": {
                "type": "long"
            },
            "content": {
                "type": "text"
            },
            "title": {
                "type": "text"
            },
            "url": {
                "type": "text"
            },
            "image_file": {
                "type": "text"
            },
            "post_date": {
                "type": "date"
            },
            "modified_date": {
                "type": "date"
            },
            "shipped_from": {
                "type": "text"
            }
        }
    }
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)