from ollama import chat


def summarize_incident(
        ticket,
        category,
        analysis):

    prompt = f"""
You are preparing an incident update for a support manager.

Create a short summary with these sections:

1. Issue Category
2. Executive Summary
3. Most Likely Root Cause
4. Recommended Next Action

Ticket:
{ticket}

Category:
{category}

Analysis:
{analysis}
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