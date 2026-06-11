# evaluator.py

import time

from classifier import classify_ticket
from metrics import summarize_metrics


def evaluate_prompt(
        dataset,
        prompt_name,
        prompt_file):

    correct = 0
    total = 0
    total_latency = 0

    failed_cases = []

    for row in dataset:

        ticket = row["ticket"]
        expected = row["expected_category"]

        start = time.time()

        prediction = classify_ticket(
            ticket,
            prompt_file
        )

        end = time.time()

        latency = end - start
        total_latency += latency

        if prediction.lower() == expected.lower():
            correct += 1
        else:
            failed_cases.append({
                "ticket": ticket,
                "expected": expected,
                "predicted": prediction
            })

        total += 1

    metrics = summarize_metrics(
        correct,
        total,
        total_latency
    )

    return {
        "prompt": prompt_name,
        "accuracy": metrics["accuracy"],
        "latency": metrics["avg_latency"],
        "failures": metrics["failures"],
        "failed_cases": failed_cases
    }