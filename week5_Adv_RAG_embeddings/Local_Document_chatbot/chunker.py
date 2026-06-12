from document_loader import (
    load_document
)


def create_chunks(
        text,
        lines_per_chunk=4):

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    chunks = []

    for i in range(
            0,
            len(lines),
            lines_per_chunk):

        chunk = "\n".join(
            lines[
                i:i +
                lines_per_chunk
            ]
        )

        chunks.append(
            chunk
        )

    return chunks


if __name__ == "__main__":

    document = load_document(
        "knowledge_base.txt"
    )

    chunks = create_chunks(
        document
    )

    for index, chunk in enumerate(
            chunks,
            start=1):

        print(
            f"\n--- Chunk {index} ---"
        )

        print(chunk)