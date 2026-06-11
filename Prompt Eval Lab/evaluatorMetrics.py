import csv
import json
import time

from classifier import classify_ticket
from prompt import PROMPT_V1,PROMPT_V2,PROMPT_V3

correct = 0
valid_json = 0
total = 0
total_latency = 0

with open(
    "Prompt Eval Lab/data/tickets.csv",
    "r",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        start = time.time()

        prediction = classify_ticket(
            row["ticket"],
            PROMPT_V1
        )

        end = time.time()

        latency = end - start

        total_latency += latency

        if prediction.lower() == row[
            "expected_category"
        ].lower():
            correct += 1

        # Example JSON validation
        try:
            json.loads(
                '{"category":"' +
                prediction +
                '"}'
            )
            valid_json += 1
        except:
            pass

        total += 1

accuracy = (
    correct / total
) * 100

json_rate = (
    valid_json / total
) * 100

avg_latency = (
    total_latency / total
)

print(
    f"Accuracy: {accuracy:.1f}%"
)

print(
    f"JSON Validity: {json_rate:.1f}%"
)

print(
    f"Average Latency: {avg_latency:.2f} seconds"
)