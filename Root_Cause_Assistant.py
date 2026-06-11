from ollama import chat

incident = """
After deployment, users receive HTTP 500 errors.
Application logs show JDBC connection timeouts.
"""

prompt = f"""
You are a senior L3 support engineer.

Analyze this incident step by step.

1. Identify the symptoms.
2. Identify the affected systems.
3. Suggest possible root causes.
4. Select the most likely root cause.
5. Recommend the next troubleshooting step.

Incident:
{incident}
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

print(
    response["message"]["content"]
)