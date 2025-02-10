import requests

# Replace with your actual Groq API Key
GROQ_API_KEY = "your_groq_api_key"

def ask_groq(question):
    url = "https://api.groq.com/v1/query"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"question": question}

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("answer", "No response received.")
    else:
        return f"Error: {response.status_code} - {response.text}"

# Chat loop
print("Groq Chatbot (type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    response = ask_groq(user_input)
    print(f"Groq: {response}")
