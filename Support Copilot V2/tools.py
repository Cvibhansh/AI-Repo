def check_server_status(server):

    data = {
        "APP01":"UP",
        "APP02":"DOWN"
    }

    return data.get(
        server,
        "UNKNOWN"
    )


def check_database_status(db):

    data = {
        "MYSQL01":"CONNECTED",
        "MYSQL02":"DISCONNECTED"
    }

    return data.get(
        db,
        "UNKNOWN"
    )