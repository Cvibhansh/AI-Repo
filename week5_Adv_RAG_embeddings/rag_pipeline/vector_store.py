from chunker import (
    load_document,
    create_chunks
)

from pathlib import Path


def generate_fake_vector(
        chunk):

    chunk = chunk.lower()

    if (
        "jdbc" in chunk
        or
        "mysql" in chunk
    ):
        return [8, 2, 1]

    if (
        "ssl" in chunk
        or
        "certificate" in chunk
    ):
        return [1, 9, 8]

    if (
        "login" in chunk
        or
        "authentication" in chunk
    ):
        return [2, 2, 9]

    if (
        "disk" in chunk
    ):
        return [6, 1, 4]

    if (
        "memory" in chunk
        or
        "heap" in chunk
    ):
        return [3, 7, 2]

    return [5, 5, 5]


def build_vector_store():

    base_dir = Path(__file__).resolve().parent 
    document_path = base_dir / "knowledge_base.txt"
    text = load_document(document_path)

    chunks = create_chunks(
        text
    )

    store = []

    for index, chunk in enumerate(
            chunks):

        store.append(
            {
                "id": index,
                "text": chunk,
                "vector":
                generate_fake_vector(
                    chunk
                )
            }
        )

    return store