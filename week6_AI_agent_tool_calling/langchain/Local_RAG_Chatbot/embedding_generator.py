import ollama


def generate_embedding(
        text):

    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )

    return response[
        "embedding"
    ]


if __name__ == "__main__":

    sample = (
        "Verify JDBC URL and "
        "database credentials."
    )

    vector = generate_embedding(
        sample
    )

    print(
        f"Vector length: "
        f"{len(vector)}"
    )

    print(
        "\nFirst 10 values:"
    )

    print(
        vector[:10]
    )