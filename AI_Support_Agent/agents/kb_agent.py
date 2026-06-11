from tools.kb_search import (
    search_kb
)


def retrieve_context(ticket):

    return search_kb(
        "jdbc"
    )