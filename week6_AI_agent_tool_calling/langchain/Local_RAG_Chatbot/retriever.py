import json

from embedding_generator import (
    generate_embedding
)

from similarity import (
    cosine_similarity
)


def retrieve(
        query,
        top_k=3):

    query_embedding = (
        generate_embedding(
            query
        )
    )

    with open(
            "vectors.json",
            "r",
            encoding="utf-8"
    ) as file:

        vectors = json.load(
            file
        )

    results = []

    for record in vectors:

        score = (
            cosine_similarity(
                query_embedding,
                record[
                    "embedding"
                ]
            )
        )

        results.append(
            {
                "file":
                record[
                    "file"
                ],

                "chunk_id":
                record[
                    "chunk_id"
                ],

                "text":
                record[
                    "text"
                ],

                "score":
                score
            }
        )

    results.sort(
        key=lambda x:
        x["score"],
        reverse=True
    )

    return results[
        :top_k
    ]


def build_context(
        matches):

    context = ""

    for match in matches:

        context += (
            match[
                "text"
            ]
            + "\n\n"
        )

    return context