from search_engine import (
    search_documents
)

from rag_engine import (
    answer_question
)


def main():

    print(
        "\n=============================="
    )
    print(
        "      LOCAL RAG DEMO"
    )
    print(
        "==============================\n"
    )

    question = input(
        "Ask a support question:\n> "
    )

    document = search_documents(
        question
    )

    if document is None:

        print(
            "\nNo relevant document found."
        )

        return

    print(
        "\n--- Retrieved Document ---\n"
    )

    print(
        document["name"]
    )

    answer = answer_question(
        question,
        document["content"]
    )

    print(
        "\n--- AI Answer ---\n"
    )

    print(answer)


if __name__ == "__main__":
    main()