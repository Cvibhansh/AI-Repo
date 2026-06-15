import json

from document_loader import (
    load_documents
)

from text_splitter import (
    split_text
)

from embedding_generator import (
    generate_embedding
)

documents = load_documents(
    "data"
)

vector_store = []

for document in documents:

    chunks = split_text(
        document[
            "content"
        ]
    )

    for index, chunk in enumerate(
            chunks):

        embedding = (
            generate_embedding(
                chunk
            )
        )

        vector_store.append(
            {
                "file":
                document[
                    "filename"
                ],

                "chunk_id":
                index + 1,

                "text":
                chunk,

                "embedding":
                embedding
            }
        )

print(
    f"Created "
    f"{len(vector_store)} "
    f"vectors."
)

with open(
        "vectors.json",
        "w",
        encoding="utf-8"
) as file:

    json.dump(
        vector_store,
        file
    )