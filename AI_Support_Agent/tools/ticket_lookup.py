import json


def lookup_ticket(ticket_id):

    with open(
        "AI_Support_Agent/tickets.json",
        "r",
        encoding="utf-8"
    ) as file:

        tickets = json.load(file)

    for ticket in tickets:
        print(f"Looking up ticket: {ticket_id}")

        if (ticket["id"].lower()==ticket_id.lower()):
            

            return ticket

    return None