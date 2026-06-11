from agents.planner_agent import (
    create_plan
)

from agents.classifier_agent import (
    classify_ticket
)

from agents.kb_agent import (
    retrieve_context
)

from agents.summary_agent import (
    generate_summary
)


def load_ticket():

    with open(
        "Multi_Agent\sample_tickets.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def main():

    ticket = load_ticket()

    print(
        "\n=========================="
    )

    print(
        " MULTI-AGENT AI DEMO "
    )

    print(
        "==========================\n"
    )

    print(
        "Planner Agent: Creating workflow..."
    )

    plan = create_plan()

    print(
        f"Workflow: {plan}\n"
    )

    print(
        "Agent 1: Classifying ticket..."
    )

    category = classify_ticket(
        ticket
    )

    print(
        f"Category: {category}\n"
    )

    print(
        "Agent 2: Searching knowledge base..."
    )

    context = retrieve_context(
        ticket
    )

    print(
        "KB article retrieved.\n"
    )

    print(
        "Agent 3: Creating summary..."
    )

    summary = generate_summary(
        ticket,
        category,
        context
    )

    print(
        "\n===== FINAL REPORT =====\n"
    )

    print(summary)


if __name__ == "__main__":
    main()