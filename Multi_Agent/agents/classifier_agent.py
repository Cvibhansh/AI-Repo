from ollama import chat


def classify_ticket(ticket):

    prompt = f"""
You are a ticket classification specialist.

Classify this incident into exactly one category:
- Database
- Security
- Infrastructure
- Application

Return ONLY the category.

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

    return (
        response["message"]["content"]
        .strip()
    )