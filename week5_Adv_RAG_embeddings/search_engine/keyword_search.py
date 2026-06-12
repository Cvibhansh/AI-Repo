from documents import DOCUMENTS


def keyword_search(query):

    query_words = set(
        query.lower().split()
    )

    results = []

    for document in DOCUMENTS:

        content_words = set(
            document["content"]
            .lower()
            .split()
        )

        score = len(
            query_words
            &
            content_words
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