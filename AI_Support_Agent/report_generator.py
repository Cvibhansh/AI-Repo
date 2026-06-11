import json
import os


REPORT_FOLDER = "AI_Support_Agent/reports"


def save_report(
        structured_data,
        summary):

    os.makedirs(
        REPORT_FOLDER,
        exist_ok=True
    )

    json_path = os.path.join(
        REPORT_FOLDER,
        "incident_report.json"
    )

    with open(
            json_path,
            "w",
            encoding="utf-8") as file:

        json.dump(
            structured_data,
            file,
            indent=4
        )

    text_path = os.path.join(
        REPORT_FOLDER,
        "incident_report.txt"
    )

    with open(
            text_path,
            "w",
            encoding="utf-8") as file:

        file.write(
            "=== AI INCIDENT REPORT ===\n\n"
        )
        file.write(
            summary
        )

    return (
        json_path,
        text_path
    )