import time
from classifier import classify_ticket

def evaluate_prompt(dataset, prompt_name, prompt_template):

    correct = 0
    total = 0
    total_latency = 0

    failures = []

    for row in dataset:

        start = time.time()

        prediction = classify_ticket(
            row["ticket"],
            prompt_template
        )

        end = time.time()

        latency = end - start
        total_latency += latency

        expected = row[
            "expected_category"
        ]

        passed = (
            prediction.lower()
            == expected.lower()
        )

        if passed:
            correct += 1
        else:
            failures.append({
                "ticket": row["ticket"],
                "expected": expected,
                "predicted": prediction
            })

        total += 1

    accuracy = (
        correct / total
    ) * 100

    avg_latency = (
        total_latency / total
    )

    return {
        "prompt": prompt_name,
        "accuracy": accuracy,
        "latency": avg_latency,
        "failures": failures
    }