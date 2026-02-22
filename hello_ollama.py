import requests

# Send a simple prompt to Ollama running locally
response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        "model": "llama3",
        "prompt": "Explain the difference between AI and Machine Learning.",
        "stream": False
    }
)

print(" Response from Llama3:")
print(response.json()["response"]) 