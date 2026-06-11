import json
from ollama import chat


def create_json(
        ticket,
        category,
        kb_context,
        ticket_info):

    prompt = f"""
    Strict instructions:
Return ONLY valid JSON.
Do not add any explanation or markdown
Respond exactly with a JSON object

{{
  "category": "",
  "ticket_status": "",
  "priority": "",
  "root_cause": "",
  "recommended_action": ""
}}

Ticket:
{ticket}

Category:
{category}

KB:
{kb_context}

Ticket Info:
{ticket_info}
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

    return json.loads(
        response["message"]["content"]
    )