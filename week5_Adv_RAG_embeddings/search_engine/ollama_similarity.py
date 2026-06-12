from ollama import chat

query = input(
    "Enter a support issue: "
)

prompt = f"""
You are an AI support tutor.

Given this issue:
{query}

Explain:
1. What category of problem it belongs to.
2. What similar issues might exist.
3. What knowledge base articles
   an engineer should look for.
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

print(
    "\nAI Analysis:\n"
)

print(
    response["message"]["content"]
)