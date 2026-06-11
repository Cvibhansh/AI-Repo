from ollama import chat

ticket = """
Production website is down.
All customers affected.
"""

prompt = f"""
Determine priority.

Rules:

P1 = Production Down
P2 = Major Impact
P3 = Minor Impact

Return JSON.

{{
  "priority":"",
  "reason":""
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
