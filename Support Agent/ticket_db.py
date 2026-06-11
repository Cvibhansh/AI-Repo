import json


def lookup_ticket(
        ticket_id):

    with open(
        "Support Agent/tickets.json",
        "r",
        encoding="utf-8"
    ) as file:

        tickets = json.load(
            file
        )

    for ticket in tickets:

        if (
            ticket["id"]
            .lower()
            ==
            ticket_id.lower()
        ):

            return ticket

    return None