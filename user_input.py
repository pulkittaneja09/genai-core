import requests

def ask_llama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    # Safe access (no KeyError)
    if "response" in data:
        return data["response"]
    else:
        return f"Error from Ollama: {data}"

user_question = input("Ask something: ")
answer = ask_llama(user_question)
print(answer)