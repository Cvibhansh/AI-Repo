from ollama import chat

response = chat(
    model='qwen2.5:7b',
    messages=[
        {
            'role': 'user',
            'content': 'Explain prompt engineering in simple terms'
        }
    ]
)

print(response['message']['content'])