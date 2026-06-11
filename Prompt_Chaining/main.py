
from pathlib import Path
from classify import classify_ticket
from root_cause import (
    analyze_root_cause
)
from summarize import (
    summarize_incident
)


def load_ticket():
    base_dir = Path(__file__).resolve().parent
    ticket_path = base_dir / "sample_tickets.txt"
    if not ticket_path.exists():
        raise FileNotFoundError(
            f"Ticket file not found: {ticket_path}"
        )

    return ticket_path.read_text(encoding="utf-8")


def main():

    ticket = load_ticket()

    print(
        "\n=============================="
    )
    print(
        "      AI SUPPORT COPILOT"
    )
    print(
        "==============================\n"
    )

    print(
        "Original Ticket:\n"
    )

    print(ticket)

    print(
        "\n------------------------------"
    )
    print(
        "Step 1: Classifying Ticket..."
    )

    category = classify_ticket(
        ticket
    )

    print(
        f"Category: {category}"
    )

    print(
        "\n------------------------------"
    )
    print(
        "Step 2: Root Cause Analysis..."
    )

    analysis = analyze_root_cause(
        ticket,
        category
    )

    print("\n")
    print(analysis)

    print(
        "\n------------------------------"
    )
    print(
        "Step 3: Incident Summary..."
    )

    summary = summarize_incident(
        ticket,
        category,
        analysis
    )

    print("\n")
    print(summary)

    print(
        "\n=============================="
    )


if __name__ == "__main__":
    main()