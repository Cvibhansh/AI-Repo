from tools import (
    AVAILABLE_TOOLS
)


def process_query(
        user_input):

    text = user_input.lower()

    # Ticket lookup
    if (
        "inc" in text
    ):

        words = (
            user_input
            .split()
        )

        for word in words:

            if (
                word.upper()
                .startswith("INC")
            ):

                tool = (
                    AVAILABLE_TOOLS[
                        "lookup_ticket"
                    ]
                )

                result = tool(
                    word
                )

                if result:

                    return (
                        f"Ticket: "
                        f"{result['id']}\n"
                        f"Status: "
                        f"{result['status']}\n"
                        f"Owner: "
                        f"{result['owner']}\n"
                        f"Priority: "
                        f"{result['priority']}"
                    )

                return (
                    "Ticket not found."
                )

    # KB search
    if (
        "jdbc" in text
        or
        "database" in text
    ):

        tool = (
            AVAILABLE_TOOLS[
                "search_kb"
            ]
        )

        return tool(
            "jdbc"
        )

    # Calculator
    if (
        "add" in text
    ):

        numbers = []

        for token in (
                text.split()
        ):

            if (
                token.isdigit()
            ):

                numbers.append(
                    int(token)
                )

        if (
            len(numbers)
            >= 2
        ):

            tool = (
                AVAILABLE_TOOLS[
                    "add_numbers"
                ]
            )

            return (
                f"Result: "
                f"{tool(numbers[0], numbers[1])}"
            )
        
    if "status" in text:
        tool = AVAILABLE_TOOLS["get_system_status"]
        return str(tool())

    return (
        "I don't know which "
        "tool to use."
    )