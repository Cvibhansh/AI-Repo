import json
from ollama import chat

ticket = """
SSL certificate expired on production server.
Users receive browser security warnings.
"""

prompt = f"""
Return ONLY valid JSON.

{{
  "category": "",
  "severity": "",
  "root_cause": "",
  "affected_component": "",
  "next_action": "",
  "estimated_priority": ""
}}

Ticket:
{ticket}
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

data = json.loads(
    response["message"]["content"]
)

print(
    json.dumps(
        data,
        indent=4
    )
)