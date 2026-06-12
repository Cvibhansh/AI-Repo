from keyword_search import (
    keyword_search
)

from semantic_search import (
    semantic_search
)


def main():

    print(
        "\n=== SEARCH COMPARISON ===\n"
    )

    query = input(
        "Enter your query: "
    )

    print(
        "\nKeyword Search Results:"
    )

    for score, title in (
            keyword_search(
                query
            )):

        print(
            f"{title:25} "
            f"Score: {score}"
        )

    print(
        "\nSemantic Search Results:"
    )

    for score, title in (
            semantic_search(
                query
            )):

        print(
            f"{title:25} "
            f"Score: {score}"
        )


if __name__ == "__main__":
    main()