from ollama import chat
import json

def create_plan(user_input):

    prompt = f"""
You are a support engineer AI planner.

Available tools:
1. search_kb
2. check_server_status
3. check_database_status

Given the user request, determine which tools are needed.

Return JSON only.

Example:

{{
    "tools":[
        "search_kb",
        "check_database_status"
    ]
}}

User Request:
{user_input}
"""

    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return json.loads(
        response["message"]["content"]
    )