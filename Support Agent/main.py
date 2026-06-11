from agent import (
    process_query
)


def main():

    print(
        "\n=========================="
    )

    print(
        "   SUPPORT AI AGENT"
    )

    print(
        "=========================="
    )

    print(
        "Type 'exit' to quit.\n"
    )

    while True:

        user_input = input(
            "> "
        )

        if (
            user_input
            .lower()
            ==
            "exit"
        ):

            break

        answer = process_query(
            user_input
        )

        print(
            "\n"
            + answer
            + "\n"
        )


if __name__ == "__main__":
    main()