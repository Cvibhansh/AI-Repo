from ollama import chat

ticket = """
User cannot login.
Password reset fails.
"""

prompt = f"""
Analyze ticket.

Return JSON only.

{{
  "category":"",
  "priority":"",
  "summary":""
}}

Ticket:
{ticket}
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