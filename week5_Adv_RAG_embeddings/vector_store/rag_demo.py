from ollama import chat

from vector_search import (
    search_vector_store
)


def get_query_vector(
        query):

    query = query.lower()

    if (
        "database" in query
        or
        "jdbc" in query
    ):
        return [8, 2, 1]

    if (
        "ssl" in query
        or
        "certificate" in query
    ):
        return [1, 9, 8]

    if (
        "login" in query
        or
        "authenticate" in query
    ):
        return [2, 2, 9]

    return [5, 5, 5]


def main():

    print(
        "\n=== SIMPLE RAG DEMO ===\n"
    )

    question = input(
        "Ask a support question: "
    )

    query_vector = (
        get_query_vector(
            question
        )
    )

    results = (
        search_vector_store(
            query_vector
        )
    )

    best_match = (
        results[0][1]
    )

    prompt = f"""
You are an IT support assistant.

User Question:
{question}

Relevant Knowledge Base Article:
{best_match['text']}

Answer the question using the
knowledge base information.
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
        "\nRetrieved Article:"
    )

    print(
        best_match["title"]
    )

    print(
        "\nAI Answer:\n"
    )

    print(
        response["message"]["content"]
    )


if __name__ == "__main__":
    main()