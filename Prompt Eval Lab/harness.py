import csv

def load_dataset():

    dataset = []

    with open(
        "Prompt Eval Lab/data/tickets.csv",
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            dataset.append(row)

    return dataset

from prompt import PROMPTS
from evaluator_return_struct import evaluate_prompt

dataset = load_dataset()

results = []

for prompt_name, prompt_text in PROMPTS.items():

    result = evaluate_prompt(
        dataset,
        prompt_name,
        prompt_text
    )

    results.append(result)




# Load Dataset
#       ↓
# For each Prompt Version
#       ↓
# Run Evaluation
#       ↓
# Collect Results
#       ↓
# Store Results




print("\n=== Evaluation Results ===\n")

print(
    f"{'Prompt':<10}"
    f"{'Accuracy':<15}"
    f"{'Latency(s)':<15}"
)

print("-" * 40)

for result in results:

    print(
        f"{result['prompt']:<10}"
        f"{result['accuracy']:<15.1f}"
        f"{result['latency']:<15.2f}"
    )



for result in results:

    print(
        f"\nFailures for "
        f"{result['prompt']}:"
    )

    for failure in result[
        "failures"
    ]:

        print(
            f"\nTicket: "
            f"{failure['ticket']}"
        )

        print(
            f"Expected: "
            f"{failure['expected']}"
        )

        print(
            f"Predicted: "
            f"{failure['predicted']}"
        )


        experiment = {
    "name": "Few-Shot Evaluation",
    "hypothesis":
        "Adding examples improves accuracy.",
    "baseline": "Prompt V2",
    "candidate": "Prompt V3"
}

print("=" * 50)
print(
    f"Experiment: "
    f"{experiment['name']}"
)

print(
    f"Hypothesis: "
    f"{experiment['hypothesis']}"
)

print("=" * 50)