from ollama import chat

incident = """
Users cannot login.

Database latency increased after patch deployment.

Error:
Connection timeout.
"""

prompt = f"""
You are a senior support engineer.

Return JSON only.

{{
  "summary":"",
  "category":"",
  "priority":"",
  "possible_causes":[],
  "recommended_actions":[]
}}

Incident:
{incident}
"""

response = chat(
    model='qwen2.5:7b',
    messages=[
        {
            'role':'user',
            'content':prompt
        }
    ]
)

print(response['message']['content'])