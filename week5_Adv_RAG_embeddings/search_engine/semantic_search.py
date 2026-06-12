from documents import DOCUMENTS


SYNONYMS = {
    "database": [
        "jdbc",
        "mysql",
        "sql"
    ],
    "connect": [
        "connection",
        "establish"
    ],
    "login": [
        "authenticate",
        "authentication"
    ]
}


def expand_query(query):

    words = query.lower().split()

    expanded = set(words)

    for word in words:

        if word in SYNONYMS:

            expanded.update(
                SYNONYMS[word]
            )

    return expanded


def semantic_search(query):

    expanded_query = (
        expand_query(query)
    )

    results = []

    for document in DOCUMENTS:

        document_words = set(
            document["content"]
            .lower()
            .split()
        )

        score = len(
            expanded_query
            &
            document_words
        )

        results.append(
            (
                score,
                document["title"]
            )
        )

    results.sort(
        reverse=True
    )

    return results