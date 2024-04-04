import requests

result = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums")
print(result.text)
