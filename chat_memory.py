import requests
conversation_history=""
def ask_llama(prompt):
    response=requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"llama3",
            "prompt":prompt,
            "stream":False
        }
    )
    data=response.json()
    if "response" in data:
        x=data["response"]
        return x;
    else:
        return f"Error from ollama:{data}"
print("chat started.Type 'exit' to stop\n")
while True:
    user_question=input("you: ")
    if user_question.lower()=="exit":
        break
    conversation_history+=f"user:{user_question}\n AI: "
    answer=ask_llama(conversation_history)
    print("Ai:",answer)
    conversation_history+=f"{answer}\n"
