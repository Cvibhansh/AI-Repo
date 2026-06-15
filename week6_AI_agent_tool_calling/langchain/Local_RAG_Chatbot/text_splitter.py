def split_text(
        text,
        chunk_size=120,
        overlap=20):

    chunks = []

    start = 0

    while (
        start
        <
        len(text)
    ):

        end = (
            start
            + chunk_size
        )

        chunk = text[
            start:end
        ]

        chunks.append(
            chunk
        )

        start = (
            end
            - overlap
        )

    return chunks



# if __name__ == "__main__":

#     sample = (
#         "This is a simple "
#         "support document used "
#         "to demonstrate text "
#         "splitting for RAG."
#     ) * 5

#     pieces = split_text(
#         sample
#     )

#     for i, piece in enumerate(
#             pieces,
#             start=1):

#         print(
#             f"\nChunk {i}"
#         )

#         print(
#             "-" * 30
#         )

#         print(
#             piece
#         )