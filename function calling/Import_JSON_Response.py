# import json
# import tools

# tool_response = '''
# {
#   "tool":"get_server_status",
#   "argument":"APP01"
# }
# '''

# result = json.loads(tool_response)

# status = tools.check_server_status(
#     result["argument"]
# )

# print(status)
















# import json

# from tools import check_server_status
# from ollama import chat

# question = "Check APP01"

# prompt = f"""
# You are a support engineer.

# Available tools:

# check_server_status(server_name)

# Return JSON only.

# User Request:
# {question}
# """

# response = chat(
#     model="qwen2.5:7b",
#     messages=[
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
# )

# tool_call = response["message"]["content"]

# print(tool_call)

# result = json.loads(tool_call)

# if result["tool"] == "check_server_status":
#     status = check_server_status(
#         result["argument"]
#     )

#     print(status)



#NO if statments

import json

from ollama import chat
import tools
import router
tool_call = """
{
  "tool":"check_database_status",
  "argument":"MYSQL01"
}

"""

request = json.loads(tool_call)

tool_name = request["tool"]

argument = request["argument"]

tool_function = router.TOOLS[tool_name]

result = tool_function(argument)

# print(result)


#human understandable response

final_prompt = f"""

Tool Result:
{result}

Provide a helpful response.
"""

final_response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role":"user",
            "content":final_prompt
        }
    ]
)

print(final_response["message"]["content"])