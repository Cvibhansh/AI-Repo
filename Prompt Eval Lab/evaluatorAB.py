import csv

from classifier import classify_ticket
from prompt import (
    PROMPT_V1,
    PROMPT_V2,
    PROMPT_V3
    )

def evaluate(prompt_template, prompt_name):

    correct = 0
    total = 0

    print(
        f"\n===== {prompt_name} =====\n"
    )

    with open(
        "Prompt Eval Lab/data/tickets.csv",
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            prediction = classify_ticket(
                row["ticket"],
                prompt_template
            )

            expected = row[
                "expected_category"
            ]

            if (
                prediction.lower()
                == expected.lower()
            ):
                correct += 1

            total += 1

            print(
                f"Ticket: {row['ticket']}"
            )
            print(
                f"Expected: {expected}"
            )
            print(
                f"Predicted: {prediction}"
            )
            print("-" * 30)

    accuracy = (
        correct / total
    ) * 100

    print(
        f"\n{prompt_name} Accuracy: {accuracy:.1f}%"
    )

    return accuracy


v1_score = evaluate(
    PROMPT_V1,
    "Prompt V1"
)

v2_score = evaluate(
    PROMPT_V2,
    "Prompt V2"
)

V3_score = evaluate(
    PROMPT_V3,
    "Prompt V3"
)

print("\n==========")
print(
    f"V1: {v1_score:.1f}%"
)
print(
    f"V2: {v2_score:.1f}%"
)
print(
    f"V3: {V3_score:.1f}%"
)

if v1_score == v2_score == V3_score:
    print(
        "ALL PROMPTS PERFORMED THE SAME!"
    )
elif V3_score >= v2_score and V3_score >= v1_score:
    print(
        "Prompt V3 wins!"
    )
elif v2_score >= v1_score and v2_score >= V3_score:
    print(
        "Prompt V2 wins!"
    )
else:
    print(
        "Prompt v1 wins!"
    )