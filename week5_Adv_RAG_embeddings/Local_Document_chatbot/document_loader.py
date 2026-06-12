from pathlib import Path


def load_document(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


if __name__ == "__main__":

    base_dir = Path(__file__).resolve().parent
    document_path = base_dir / "knowledge_base.txt"
    document = load_document(document_path)

    print(document)