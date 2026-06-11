import json
from ollama import chat
from pathlib import Path
from json_validator import (
    validate_json
)


def load_ticket():
    base_dir = Path(__file__).resolve().parent
    ticket_path = base_dir / "sample_tickets.txt"
    if not ticket_path.exists():
        raise FileNotFoundError(
            f"Ticket file not found: {ticket_path}"
        )

    return ticket_path.read_text(encoding="utf-8")


def analyze_ticket(ticket):

    prompt = f"""
You are a senior enterprise support engineer.

Analyze the following incident.

Return ONLY a valid JSON object with this structure:

{{
    "category": "",
    "root_cause": "",
    "severity": "",
    "next_action": "",
    "affected_component": "",
    "estimated_priority": ""    
}}

Rules:
- Do not add markdown.
- Do not use ```json blocks.
- Do not explain the answer.
- Return only valid JSON.

Ticket:
{ticket}
"""

    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return (
        response["message"]["content"]
        .strip()
    )


def main():

    ticket = load_ticket()

    print(
        "\n=== Original Ticket ===\n"
    )

    print(ticket)

    json_output = analyze_ticket(
        ticket
    )

    print(
        "\n=== Model Output ===\n"
    )

    print(json_output)
    status, message = validate_json(
    json_output)
    print("\nValidation:")
    print(message)
    

    try:

        parsed = json.loads(
            json_output
        )

        print(
            "\n=== Parsed JSON ===\n"
        )

        print(
            f"Category    : {parsed['category']}"
        )

        print(
            f"Root Cause  : {parsed['root_cause']}"
        )

        print(
            f"Severity    : {parsed['severity']}"
        )

        print(
            f"Next Action : {parsed['next_action']}"
        )
        print(
            f"Affected Component : {parsed['affected_component']}"
        )
        print(
            f"Estimated Priority : {parsed['estimated_priority']}"
        )
        

    except json.JSONDecodeError:

        print(
            "\n❌ Invalid JSON returned!"
        )


if __name__ == "__main__":
    main()