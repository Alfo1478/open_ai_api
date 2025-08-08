
# creating a chatbot using the OpenAI API to generate responses to the following Parisian tourist questions like:
# How far away is the Louvre from the Eiffel Tower (in miles) if you are driving? / Where is the Arc de Triomphe? / What are the must-see artworks at the Louvre Museum?
# Importing 
import os
from openai import OpenAI

# Define the model to use
model = "gpt-3.5-turbo"

# Define the client
client = OpenAI(api_key=os.environ["OPENAI"])

# Define parameters for the model
temperature = 0.0
max_completion_tokens = 100

# Define initial conversation
conversation = [
    {"role": "system",
     "content": "You are an assistant that aims to help answering questions about Paris, who provides short, and simple answers"},
    {"role": "user",
     "content": "what is the most important place in Paris"}
]

# Define some user questions
questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

for q in questions:
    print("User:", q)
    # From the user questions list, here are set in a desirable format for get them into the API consult    
    input_dict = {"role": "user", "content": q}
    conversation.append(input_dict)
    # Api calls
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        max_completion_tokens=max_completion_tokens,
        messages=conversation
    )

    # Response from the model
    resp = response.choices[0].message.content

    resp_dict = {"role": "assistant", "content": resp}
    conversation.append(resp_dict)
    print("Assistant: ", resp, "\n")
