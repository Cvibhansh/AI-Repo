from ollama import chat

with open("RAG/deployment.txt", "r") as f:
    context = f.read()

question = "How do I restart Order Service?"

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