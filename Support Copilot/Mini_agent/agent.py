from tools import check_server_status, search_kb

question = """
Database DB01 is down after deployment.
"""

print("User:")
print(question)

print("\nAgent Reasoning:")
print("1. Need to check server status.")
status = check_server_status("DB01")
print(f"Observation: DB01 = {status}")

print("\n2. Need deployment knowledge.")
kb = search_kb("deployment")
print(f"Observation: {kb}")

print("\nFinal Answer:")
print(f"DB01 is {status}. Based on the KB, the issue may be related to deployment configuration or version mismatch.")