from ollama import chat

from retriever import (
    retrieve
)


def build_context(
        chunks):

    context = ""

    for index, chunk in enumerate(
            chunks,
            start=1):

        context += (
            f"\n--- "
            f"Chunk {index} ---\n"
        )

        context += (
            chunk["text"]
            + "\n"
        )

    return context


def main():

    print(
        "\n=== ADVANCED RAG PIPELINE ===\n"
    )

    question = input(
        "Ask an IT support question: "
    )

    retrieved_chunks = (
        retrieve(
            question,
            top_k=2
        )
    )

    context = build_context(
        retrieved_chunks
    )

    prompt = f"""
You are an enterprise IT support assistant.

Answer the user's question using
ONLY the information contained
in the retrieved knowledge base.

User Question:
{question}

Retrieved Context:
{context}

If the answer is not available
in the context, say:
"I could not find that information
in the knowledge base."
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
        "\n=== RETRIEVED CHUNKS ==="
    )

    print(context)

    print(
        "\n=== AI ANSWER ===\n"
    )

    print(
        response["message"]["content"]
    )

    print("\nRetrieved Chunks:")
    for chunk in retrieved_chunks:
        print("-" * 30)
        print(chunk["text"][:60] + "...")


if __name__ == "__main__":
    main()