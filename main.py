import os
from pydantic import BaseModel, Field
from typing import List
from groq import Groq
import instructor

# Set up API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Ensure you set this in your environment

# Define response model
class ResponseModel(BaseModel):
    name: str
    facts: List[str] = Field(..., description="A list of facts about the subject")

# Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)

# Connect Instructor to Groq
client = instructor.from_groq(client, mode=instructor.Mode.TOOLS)

def ask_groq(question):
    """Function to send user input to Groq API and get a response."""
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": question}],
        response_model=ResponseModel,
    )
    return response.model_dump_json(indent=2)

# Start Chat Loop
print("Welcome to Groq Chatbot! (Type 'quit' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break  # This will properly exit the loop
    response = ask_groq(user_input)
    print(f"Groq: {response}")

