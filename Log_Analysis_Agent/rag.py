import os

def load_kb():

    context = ""

    for file in os.listdir("Log_Analysis_Agent/docs"):
        with open(f"Log_Analysis_Agent/docs/{file}", "r", encoding="utf-8") as f:
            context += f.read() + "\n"

    return context