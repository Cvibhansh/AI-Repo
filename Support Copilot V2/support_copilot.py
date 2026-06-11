from ollama import chat
from planner import create_plan
from rag import load_kb

ticket = input(
    "Paste Ticket or Log:\n"
)

plan = create_plan(ticket)

print("Execution Plan:")
print(plan)

kb_context = load_kb()

prompt = f"""
You are a senior L3 support engineer.

Use the provided knowledge base.

Return JSON only.

Format:

{{
  "category":"",
  "priority":"",
  "summary":"",
  "possible_causes":[],
  "recommended_actions":[]
}}

Knowledge Base:
{kb_context}

User Input:
{ticket}
"""

response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role":"system",
            "content":"You are an expert support engineer."
        },
        {
            "role":"user",
            "content":prompt
        }
    ]
)

analysis = response[
    "message"
]["content"]

print(analysis)

incident_prompt = f"""
Generate a short incident report.

Analysis:
{analysis}

Audience:
Support Manager

Limit:
5 bullet points.
"""

incident = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role":"user",
            "content":incident_prompt
        }
    ]
)

print(
    incident["message"]["content"]
)