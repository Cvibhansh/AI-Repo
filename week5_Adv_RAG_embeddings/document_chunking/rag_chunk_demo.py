from ollama import chat

from chunk_store import (
    build_chunk_store
)


def retrieve_chunk(
        question,
        store):

    question = (
        question.lower()
    )

    if (
        "jdbc" in question
        or
        "database" in question
    ):

        return store[0]["text"]

    if (
        "ssl" in question
        or
        "certificate" in question
    ):

        return store[3]["text"]

    if (
        "login" in question
        or
        "authenticate" in question
    ):

        return store[5]["text"]

    return store[0]["text"]


def main():

    print(
        "\n=== CHUNKED RAG DEMO ===\n"
    )

    question = input(
        "Ask a support question: "
    )

    store = build_chunk_store()

    context = retrieve_chunk(
        question,
        store
    )

    prompt = f"""
You are an enterprise IT support assistant.

Question:
{question}

Relevant knowledge base chunk:
{context}

Answer using only the information
provided in the knowledge base chunk.
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

    print(
        "\nRetrieved Chunk:\n"
    )

    print(
        context
    )

    print(
        "\nAI Answer:\n"
    )

    print(
        response["message"]["content"]
    )


if __name__ == "__main__":
    main()