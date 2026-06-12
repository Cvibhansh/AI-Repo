from vector_store import (
    build_vector_store
)


def get_query_vector(
        question):

    question = (
        question.lower()
    )

    if (
        "jdbc" in question
        or
        "database" in question
    ):
        return [8, 2, 1]

    if (
        "ssl" in question
        or
        "certificate" in question
    ):
        return [1, 9, 8]

    if (
        "login" in question
        or
        "authenticate" in question
    ):
        return [2, 2, 9]

    if (
        "disk" in question
    ):
        return [6, 1, 4]

    if (
        "memory" in question
        or
        "outofmemory" in question
    ):
        return [3, 7, 2]

    return [5, 5, 5]


def calculate_distance(
        a,
        b):

    return sum(
        abs(
            x - y
        )
        for x, y in zip(
            a,
            b
        )
    )


def retrieve(
        question,
        top_k=2):

    query_vector = (
        get_query_vector(
            question
        )
    )

    store = (
        build_vector_store()
    )

    results = []

    for item in store:

        distance = (
            calculate_distance(
                query_vector,
                item["vector"]
            )
        )

        results.append(
            (
                distance,
                item
            )
        )

    results.sort(
        key=lambda x: x[0]
    )

    return [
        item
        for (
            _,
            item
        ) in results[
            :top_k
        ]
    ]