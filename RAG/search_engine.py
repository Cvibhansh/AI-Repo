import os


KB_FOLDER = "RAG/docs"


def load_documents():

    documents = []

    for filename in os.listdir(
            KB_FOLDER):

        path = os.path.join(
            KB_FOLDER,
            filename
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            documents.append({
                "name": filename,
                "content": file.read()
            })

    return documents


def search_documents(
        question):

    documents = load_documents()

    question = question.lower()

    best_match = None
    best_score = 0

    for doc in documents:

        score = 0

        words = question.split()

        for word in words:

            if word in doc[
                "content"
            ].lower():

                score += 1

        if score > best_score:

            best_score = score
            best_match = doc

    return best_match