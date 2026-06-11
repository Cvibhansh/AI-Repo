from ollama import chat


def generate_summary(
        ticket,
        category,
        kb_context):

    prompt = f"""
You are an incident manager.

Using the information below, prepare a concise incident report.

Ticket:
{ticket}

Category:
{category}

Knowledge Base Context:
{kb_context}

Include:
1. Issue Category
2. Executive Summary
3. Recommended Next Step
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