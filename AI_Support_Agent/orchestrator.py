from agents.classifier_agent import classify
from agents.kb_agent import retrieve_context
from agents.json_agent import create_json
from agents.summary_agent import create_summary

from tools.ticket_lookup import lookup_ticket

from report_generator import save_report


from pathlib import Path

def load_ticket():
    base_dir = Path(__file__).resolve().parent
    ticket_path = base_dir / "sample_ticket.txt"
    if not ticket_path.exists():
        raise FileNotFoundError(f"Ticket file not found: {ticket_path}")
    return ticket_path.read_text(encoding="utf-8")


def extract_ticket_id(ticket):

    for word in ticket.split():

        if (
            word.upper()
            .startswith("INC")
        ):

            return word

    return None


def main():

    print(
        "\n==================================="
    )

    print(
        " ENTERPRISE AI SUPPORT COPILOT "
    )

    print(
        "===================================\n"
    )

    ticket = load_ticket()

    print(
        "Step 1: Classifying incident..."
    )

    category = classify(
        ticket
    )

    print(
        f"Category: {category}"
    )

    print(
        "\nStep 2: Searching KB..."
    )

    kb_context = retrieve_context(
        ticket
    )

    print(
        "Knowledge base context retrieved."
    )

    print(
        "\nStep 3: Looking up ticket..."
    )

    ticket_info = lookup_ticket(
        extract_ticket_id(
            ticket
        )
    )

    print(
        ticket_info
    )

    print(
        "\nStep 4: Creating structured JSON..."
    )

    structured_data = create_json(
        ticket,
        category,
        kb_context,
        ticket_info
    )

    print(
        structured_data
    )

    print(
        "\nStep 5: Generating executive summary..."
    )

    summary = create_summary(
        structured_data
    )

    print(
        "\nStep 6: Saving report..."
    )

    json_file, text_file = save_report(
        structured_data,
        summary
    )

    print(
        "\n===== FINAL EXECUTIVE SUMMARY =====\n"
    )

    print(summary)

    print(
        "\nReports generated:"
    )

    print(
        f"- {json_file}"
    )

    print(
        f"- {text_file}"
    )


if __name__ == "__main__":
    main()