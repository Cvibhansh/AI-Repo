from pathlib import Path


def load_documents(
        folder):

    documents = []

    path = Path(
        folder
    )

    for file in path.iterdir():

        if file.is_file():

            text = file.read_text(
                encoding="utf-8"
            )

            documents.append(
                {
                    "filename":
                    file.name,

                    "content":
                    text
                }
            )

    return documents


if __name__ == "__main__":

    docs = load_documents(
        "data"
    )

    for doc in docs:

        print(
            "=" * 50
        )

        print(
            doc[
                "filename"
            ]
        )

        print(
            "-" * 50
        )

        print(
            doc[
                "content"
            ]
        )