from chunker import (
    read_document,
    create_chunks
)
from pathlib import Path

def build_chunk_store():

    base_dir = Path(__file__).resolve().parent
    document_path = base_dir / "knowledge_base.txt"
    document = read_document(
        document_path
    )

    chunks = create_chunks(
        document
    )

    store = []

    for index, chunk in enumerate(
            chunks):

        fake_vector = [
            index + 1,
            len(
                chunk.split()
            ),
            len(
                chunk
            ) % 10
        ]

        store.append(
            {
                "id": index,
                "text": chunk,
                "vector": fake_vector
            }
        )

    return store


if __name__ == "__main__":

    vector_store = (
        build_chunk_store()
    )

    for item in (
            vector_store):

        print(
            item
        )