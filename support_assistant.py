from ollama import chat


ticket = "Application crashes after login"

prompt = f"""      
Return JSON only  
{{
  "summary":"...",
  "category":"...",
  "priority":"...",
  "possible_causes":[...],
  "recommended_actions":[...]
}}
Ticket: {ticket}
"""


response = chat(
    model='qwen2.5:7b', 
    messages=[
        {
            'role':'system',
            'content':'You are a senior support engineer. Analyze the ticket and provide a structured response in JSON format as per the template provided.'
        },
        {
            'role':'user',
            'content':prompt
        }
    ]


)
print(response['message']['content'])
