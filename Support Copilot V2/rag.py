import os

def load_kb():

    context = ""

    for file in os.listdir("Support Copilot V2/docs"):

        with open(
            f"Support Copilot V2/docs/{file}",
            "r",
            encoding="utf-8"
        ) as f:

            context += (
                f"\n--- {file} ---\n"
            )

            context += f.read()

    return context