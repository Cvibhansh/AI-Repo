from ollama import chat
from prompt import PROMPTS

def classify_ticket(ticket, prompt_template):

    prompt = f"""
{prompt_template}

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

    return response["message"]["content"].strip()