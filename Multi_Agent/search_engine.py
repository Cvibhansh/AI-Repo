import os

KB_FOLDER = "Multi_Agent\docs"


def search_documents(query):

    best_match = None
    best_score = 0

    for filename in os.listdir(KB_FOLDER):

        path = os.path.join(
            KB_FOLDER,
            filename
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        score = 0

        for word in (
                query.lower().split()
        ):

            if (
                word
                in
                content.lower()
            ):

                score += 1

        if score > best_score:

            best_score = score

            best_match = {
                "file": filename,
                "content": content
            }

    return best_match