from Kb_article import ARTICLES


def calculate_similarity(
        query_words,
        article_words):

    common_words = (
        query_words
        &
        article_words
    )

    return len(
        common_words
    )


def search(query):

    query_words = set(
        query
        .lower()
        .split()
    )

    best_article = None
    best_score = -1

    for article in ARTICLES:

        score = calculate_similarity(
            query_words,
            article["keywords"]
        )

        print(
            f"{article['title']} "
            f"-> Score: {score}"
        )

        if score > best_score:

            best_score = score
            best_article = article

    return best_article


def main():

    print(
        "\n=== EMBEDDING DEMO ===\n"
    )

    query = input(
        "Ask a question: "
    )

    result = search(
        query
    )

    print(
        "\nMost similar article:"
    )

    print(
        result["title"]
    )


if __name__ == "__main__":
    main()