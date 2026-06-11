from search_engine import (
    search_documents
)


def retrieve_context(ticket):

    result = search_documents(
        ticket
    )

    if result:

        return (
            result["content"]
        )

    return (
        "No relevant knowledge base "
        "document found."
    )