from pathlib import Path

from chunker import (
    create_chunks
)

from document_loader import (
    load_document
)


def retrieve_chunks(
        question):

    base_dir = Path(__file__).resolve().parent
    document_path = base_dir / "knowledge_base.txt"
    document = load_document(document_path)

    chunks = create_chunks(
        document
    )

    question = (
        question.lower()
    )

    results = []

    for chunk in chunks:

        score = 0

        words = (
            chunk.lower()
            .split()
        )

        for token in (
                question
                .split()):

            if token in words:
                score += 1

        results.append(
            (
                score,
                chunk
            )
        )

    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return [
        chunk
        for (
            score,
            chunk
        ) in results[:2]
    ]


if __name__ == "__main__":

    query = input(
        "Enter a question: "
    )

    matches = (
        retrieve_chunks(
            query
        )
    )

    print(
        "\nRetrieved Chunks:\n"
    )

    for chunk in matches:
        print("-" * 40)
        print(chunk)