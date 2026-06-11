from ticket_db import (
    lookup_ticket
)

from kb_search import (
    search_kb
)


def add_numbers(
        a,
        b):

    return a + b

def get_system_status():

    return {
        "database": "Healthy",
        "application": "Healthy",
        "web_server": "Warning"
    }

AVAILABLE_TOOLS = {
    "lookup_ticket":
        lookup_ticket,

    "search_kb":
        search_kb,

    "add_numbers":
        add_numbers,

    "get_system_status":
        get_system_status
}