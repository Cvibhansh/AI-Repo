from vector_store import VECTOR_STORE


def calculate_distance(
        vector1,
        vector2):

    total = 0

    for a, b in zip(
            vector1,
            vector2):

        total += abs(
            a - b
        )

    return total


def search_vector_store(
        query_vector):

    results = []

    for document in VECTOR_STORE:

        distance = (
            calculate_distance(
                query_vector,
                document["vector"]
            )
        )

        results.append(
            (
                distance,
                document
            )
        )

    results.sort(
        key=lambda x: x[0]
    )

    return results





if __name__ == "__main__":

    print(
        "\n=== VECTOR SEARCH ===\n"
    )

    query_vector = [
        8, 2, 1
    ]

    results = (
        search_vector_store(
            query_vector
        )
    )

    for (
            distance,
            document
    ) in results:

        print(
            f"{document['title']:25}"
            f" Distance: {distance}"
        )
        print(
          "The smallest distance means the most similar document."
        )