import os


def search_kb(keyword):

    folder = "AI_Support_Agent/knowledge_base"

    for filename in os.listdir(folder):

        path = os.path.join(
            folder,
            filename
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

            if (
                keyword.lower()
                in
                content.lower()
            ):

                return content

    return (
        "No KB article found."
    )