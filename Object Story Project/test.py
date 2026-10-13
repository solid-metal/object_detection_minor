import requests

res = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "tinyllama",
        "prompt": "Say hello",
        "stream": False
    }
)

print(res.text)