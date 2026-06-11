# report_generator.py

from datetime import datetime


def generate_report(results,
                    output_file="evaluation_report.md"):

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as report:

        report.write(
            "# Prompt Evaluation Report\n\n"
        )

        report.write(
            f"Generated: "
            f"{datetime.now()}\n\n"
        )

        report.write(
            "## Summary\n\n"
        )

        report.write(
            "| Prompt | Accuracy | Avg Latency (s) | Failures |\n"
        )

        report.write(
            "|--------|-----------|-----------------|----------|\n"
        )

        for result in results:

            report.write(
                f"| {result['prompt']} "
                f"| {result['accuracy']:.1f}% "
                f"| {result['latency']:.2f} "
                f"| {result['failures']} |\n"
            )

        report.write("\n")

        report.write(
            "## Detailed Failure Analysis\n\n"
        )

        for result in results:

            report.write(
                f"### {result['prompt']}\n\n"
            )

            if len(
                result["failed_cases"]
            ) == 0:

                report.write(
                    "✅ No failures.\n\n"
                )

                continue

            for index, failure in enumerate(
                result["failed_cases"],
                start=1
            ):

                report.write(
                    f"#### Failure {index}\n\n"
                )

                report.write(
                    f"**Ticket:** "
                    f"{failure['ticket']}\n\n"
                )

                report.write(
                    f"**Expected:** "
                    f"{failure['expected']}\n\n"
                )

                report.write(
                    f"**Predicted:** "
                    f"{failure['predicted']}\n\n"
                )

        report.write(
            "---\n"
        )

        report.write(
            "Report generated automatically "
            "by Prompt Evaluation Lab.\n"
        )

    print(
        f"\nReport saved to "
        f"'{output_file}'"
    )