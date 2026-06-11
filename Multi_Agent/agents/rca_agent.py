from ollama import chat


def analyze_root_cause(
        ticket,
        kb_context):

    prompt = f"""
You are a senior support engineer.

Based on the incident and KB information,
identify the most likely root cause.

Incident:
{ticket}

KB:
{kb_context}
"""

    response = chat(
        model="llama3.2",
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