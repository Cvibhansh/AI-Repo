from pathlib import Path

def read_document(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def create_chunks(
        text,
        lines_per_chunk=3):

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    chunks = []

    for index in range(
            0,
            len(lines),
            lines_per_chunk):

        chunk = "\n".join(
            lines[
                index:index +
                lines_per_chunk
            ]
        )

        chunks.append(
            chunk
        )

    return chunks


if __name__ == "__main__":

    base_dir = Path(__file__).resolve().parent
    document_path = base_dir / "knowledge_base.txt"
    document = read_document(
        document_path
    )

    chunks = create_chunks(
        document
    )

    print(
        "\n=== DOCUMENT CHUNKS ===\n"
    )

    for i, chunk in enumerate(
            chunks,
            start=1):

        print(
            f"Chunk {i}"
        )

        print(
            "------------------"
        )

        print(chunk)

        print()