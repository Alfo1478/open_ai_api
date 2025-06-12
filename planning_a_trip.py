
# creating a chatbot using the OpenAI API to generate responses to the following Parisian tourist questions like:
# How far away is the Louvre from the Eiffel Tower (in miles) if you are driving? / Where is the Arc de Triomphe? / What are the must-see artworks at the Louvre Museum?
import os
from openai import OpenAI

# Define the model to use
model = "gpt-3.5-turbo"

# Define the client
client = OpenAI(api_key=os.environ["OPENAI"])


temperature= 0.0
max_completion_tokens=100

messages=[{"role":"system","content":"You are an assitant that aims to help answering questions about Paris, who provides short, and simple answers"}]
user_questions=["How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
           "Where is the Arc de Triomphe?",
           "What are the must-see artworks at the Louvre Museum?"]

for q in user_questions:
    print("User:", q)
# From the user questions list, here are set in a desirable format for get them into the API consult    
    user_dict={"role":"user","content":q}
    messages.append(user_dict)
# Api calls
    response=client.chat.completions.create(
        model=model,
        temperature=temperature,
        max_completion_tokens=max_completion_tokens,
        messages=messages
    )

    conversation ={"role":"assistant", "content":response.choices[0].message.content}
    messages.append(conversation)
    print("Assistant: ", response.choices[0].message.content, "\n")

    
