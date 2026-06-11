from ollama import chat


def classify(ticket):

    prompt = f"""
You are an incident classifier.

Choose exactly one category:
- Database
- Security
- Infrastructure
- Application

Return only the category.

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