from ollama import chat

ticket = """
Application crashes after login.
"""

prompt = f"""
Classify this ticket.

Categories:
- Bug
- Feature Request
- Question

Ticket:
{ticket}

Return only category.
"""

response = chat(
    model='qwen2.5:7b',
    messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ]
)

print(response['message']['content'])