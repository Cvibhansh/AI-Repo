import json


REQUIRED_FIELDS = [
    "category",
    "root_cause",
    "severity",
    "next_action",
    "affected_component",
    "estimated_priority"
]


def validate_json(
        json_text):

    try:

        data = json.loads(
            json_text
        )

    except json.JSONDecodeError:

        return (
            False,
            "Invalid JSON"
        )

    missing = []

    for field in REQUIRED_FIELDS:

        if field not in data:
            missing.append(
                field
            )

    if len(missing) > 0:

        return (
            False,
            f"Missing fields: {missing}"
        )

    return (
        True,
        "JSON validation successful"
    )