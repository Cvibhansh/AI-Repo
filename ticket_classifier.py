# ticket_classifier.py

from ollama import chat

ticket = """
Application crashes after login.
Users receive HTTP 500 errors.
Issue started after deployment.
"""

prompt = f"""
You are a support engineer.

Classify the ticket.

Categories:
- Bug
- Infrastructure
- Database
- Security
- Feature Request

Return JSON only.

{{
  "category":""
}}

Ticket:
{ticket}
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