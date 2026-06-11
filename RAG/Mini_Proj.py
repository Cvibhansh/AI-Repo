import os

from ollama import chat

documents = []

for file in os.listdir("RAG/docs"):
    with open(f"RAG/docs/{file}", "r") as f:
        documents.append(f.read())

context = "\n\n".join(documents)

question = input("Ask question: ")

prompt = f"""
Answer using only the provided context.

Context:
{context}

Question:
{question}
"""

response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])