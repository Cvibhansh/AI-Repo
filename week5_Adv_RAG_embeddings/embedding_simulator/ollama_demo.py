from ollama import chat

query = input(
    "Enter a support issue: "
)

prompt = f"""
You are an AI tutor.

Explain what kind of IT problem this is
and what similar issues it might relate to.

Issue:
{query}
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
    "\nAI Explanation:\n"
)

print(
    response["message"]["content"]
)