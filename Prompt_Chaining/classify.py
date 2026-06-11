from ollama import chat


def classify_ticket(ticket):

    prompt = f"""
You are a senior L3 support engineer.

Classify the following support ticket into exactly one category.

Categories:
- Application
- Database
- Infrastructure
- Security
- Feature Request

Return ONLY the category name.

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