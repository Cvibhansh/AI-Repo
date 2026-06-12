from ollama import chat

from retriever import (
    retrieve_chunks
)


def build_context(
        chunks):

    context = ""

    for index, chunk in enumerate(
            chunks,
            start=1):

        context += (
            f"\n=== "
            f"Chunk {index} "
            f"===\n"
        )

        context += (
            chunk
            + "\n"
        )

    return context


def main():

    print(
        "\n=================================="
    )

    print(
        "   LOCAL DOCUMENT CHATBOT"
    )

    print(
        "==================================\n"
    )

    while True:

        question = input(
            "\nAsk a question "
            "(type 'exit' to quit): "
        )

        if (
            question
            .lower()
            ==
            "exit"
        ):

            print(
                "\nGoodbye!"
            )

            break

        retrieved = (
            retrieve_chunks(
                question
            )
        )

        context = (
            build_context(
                retrieved
            )
        )

        prompt = f"""
You are an enterprise IT support assistant.

Use ONLY the information
provided below.

Knowledge Base:
{context}

User Question:
{question}

If the answer cannot be found,
say:
'I could not find this information
in the current knowledge base.'
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
            "\n----- Retrieved Context -----"
        )

        print(
            context
        )

        print(
            "\n----- AI Answer -----\n"
        )

        print(
            response[
                "message"
            ][
                "content"
            ]
        )


if __name__ == "__main__":
    main()  