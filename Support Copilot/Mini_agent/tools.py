def check_server_status(server):
    data = {
        "APP01": "DOWN",
        "APP02": "UP"
    }
    return data.get(server, "UNKNOWN")

def check_database_status(db):
    data = {
        "DB01": "UP",
        "DB02": "DOWN"
    }
    return data.get(db, "UNKNOWN")


def search_kb(topic):
    kb = {
        "deployment": "Deployment failures may occur because of missing configuration or version mismatch."
    }
    return kb.get(topic.lower(), "No KB article found.")