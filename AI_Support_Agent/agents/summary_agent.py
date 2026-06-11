from ollama import chat


def create_summary(
        structured_data):

    prompt = f"""
You are an incident manager.

Using the structured information below,
write a short executive summary.

Data:
{structured_data}

Include:
1. Issue Summary
2. Business Impact
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