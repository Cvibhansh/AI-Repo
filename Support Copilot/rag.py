import os

def search_kb(question):

    context = ""

    for file in os.listdir("Support Copilot/docs"):

        with open(f"Support Copilot/docs/{file}", "r") as f:
            context += f.read() + "\n"

    return context