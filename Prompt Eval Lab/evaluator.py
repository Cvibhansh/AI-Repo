import csv

from classifier import classify_ticket

correct = 0
total = 0

with open(
    "Prompt Eval Lab/data/tickets.csv",
    "r",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        prediction = classify_ticket(
            row["ticket"]
        )

        expected = row[
            "expected_category"
        ]

        print(
            f"Ticket: {row['ticket']}"
        )

        print(
            f"Expected: {expected}"
        )

        print(
            f"Predicted: {prediction}"
        )

        print("-" * 40)

        if prediction.lower() == expected.lower():
            correct += 1

        total += 1

accuracy = (
    correct / total
) * 100

print(
    f"\nAccuracy: {accuracy:.1f}%"
)