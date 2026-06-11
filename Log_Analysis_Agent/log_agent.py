# with open("Log_Analysis_Agent/docs/sample_log.txt", "r", encoding="utf-8") as f:
#     log_data = f.read()

#instead of reading from file, we will take log input from user
log_data = input(
    "Paste application log:\n"
)



from rag import load_kb
from ollama import chat

context = load_kb()

prompt = f"""
You are a senior L3 support engineer.

Analyze the application log.

Use the provided knowledge base.

Return JSON only.

Format:

{{
  "error_type":"",
  "severity":"",
  "summary":"",
  "possible_causes":[],
  "recommended_actions":[]
}}

Knowledge Base:
{context}

Log:
{log_data}
"""






response = chat(
    model="qwen2.5:7b",  # Replace with your model name
    messages=[
        {
            "role": "system",
            "content": "You are an expert Java, Linux, and database support engineer."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])


incident_prompt = f"""
Create a short incident summary for management.

Analysis:
{response["message"]["content"]}

Keep it under 5 lines.
"""

summary_response = chat(
    model="qwen2.5:7b",  # Replace with your model name
    messages=[
        {
            "role": "user",
            "content": incident_prompt
        }
    ]
)

print(summary_response["message"]["content"])