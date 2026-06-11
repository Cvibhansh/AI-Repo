from ollama import chat


def answer_question(
        question,
        context):

    prompt = f"""
You are an enterprise support assistant.

Answer the user's question using ONLY the provided context.

If the answer is not present in the context,
say:
"I could not find that information in the knowledge base."

Context:
{context}

Question:
{question}
"""

    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return (
        response["message"]["content"]
        .strip()
    )