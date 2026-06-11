from ollama import chat


def analyze_root_cause(
        ticket,
        category):

    prompt = f"""
You are an experienced enterprise support engineer.

Analyze the incident step by step.

Step 1: Identify the key symptoms.
Step 2: Identify the affected components.
Step 3: List possible root causes.
Step 4: Select the most likely root cause.
Step 5: Recommend the next troubleshooting action.

Issue Category:
{category}

Incident:
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