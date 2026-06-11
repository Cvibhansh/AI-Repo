from ollama import chat
from pathlib import Path

def load_prompt(path):

    base_dir = Path(__file__).resolve().parent

    with open(
        base_dir / path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def classify_ticket(
    ticket,
    prompt_file
):

    prompt = load_prompt(
        prompt_file
    )

    full_prompt = f"""
{prompt}

Ticket:
{ticket}
"""

    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    return response[
        "message"
    ]["content"].strip()