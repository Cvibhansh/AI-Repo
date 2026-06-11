from ollama import chat
from rag import search_kb



ticket = input("Paste Ticket:\n")

context = search_kb(ticket)

prompt = f"""
You are a senior support engineer.

Use the provided knowledge base.

Priority Rules:

P1 = Production down

P2 = Major user impact

P3 = Minor issue

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
{context}

Incident:
{ticket}
"""


response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role":"system",
            "content":"You are a senior support engineer."
        },
        {
            "role":"user",
            "content":prompt
        }
    ]
)

print(response["message"]["content"])