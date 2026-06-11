from ollama import chat
from tools import check_server_status


user_question = input("check status")

prompt = f"""
You are a support engineer.

Available tools:

1. check_server_status(server_name)
2. check_database_status(db_name)

If user asks for server status,
return JSON only.

Example:

{{
  "tool":"check_server_status",
  "argument":"APP01"
}}

User Request:
{user_question}

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