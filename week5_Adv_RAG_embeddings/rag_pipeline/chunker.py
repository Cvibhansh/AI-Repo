def load_document(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


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
                i:i + lines_per_chunk
            ]
        )

        chunks.append(
            chunk
        )

    return chunks