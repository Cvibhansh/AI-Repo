# harness.py

import csv
from pathlib import Path

from prompts import PROMPT_FILES
from evaluator import evaluate_prompt
from report_generator import generate_report


def load_dataset():

    dataset = []
    base_dir = Path(__file__).resolve().parent

    with open(
        base_dir / "data" / "tickets.csv",
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            dataset.append(row)

    return dataset


def main():

    dataset = load_dataset()

    results = []

    print("\n===== Prompt Evaluation Lab =====\n")

    for prompt_name, prompt_file in PROMPT_FILES.items():

        print(
            f"Evaluating {prompt_name}..."
        )

        result = evaluate_prompt(
            dataset,
            prompt_name,
            prompt_file
        )

        results.append(result)

    print("\n===== Results =====\n")

    print(
        f"{'Prompt':<10}"
        f"{'Accuracy':<15}"
        f"{'Latency(s)':<15}"
        f"{'Failures':<10}"
    )

    print("-" * 55)

    for result in results:

        print(
            f"{result['prompt']:<10}"
            f"{result['accuracy']:<15.1f}"
            f"{result['latency']:<15.2f}"
            f"{result['failures']:<10}"
        )

    generate_report(results)


if __name__ == "__main__":
    main()