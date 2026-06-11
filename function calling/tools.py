# tools.py

def check_server_status(server):
    servers = {
        "APP01": "UP",
        "APP02": "DOWN"
    }

    return servers.get(server, "Unknown Server")


def check_database_status(database):
    databases = {
        "MYSQL01": "CONNECTED",
        "MYSQL02": "DISCONNECTED"
    }

    return databases.get(database, "Unknown Database")


def get_cpu_usage(server):
    cpu = {
        "APP01": "34%",
        "APP02": "89%"
    }

    return cpu.get(server, "Unknown Server")


def get_disk_space(server):
    disk = {
        "APP01": "72%",
        "APP02": "91%"
    }

    return disk.get(server, "Unknown Server")

def get_application_version(app):
    versions = {
        "APP01": "8.2.1",
        "APP02": "8.1.4"
    }

    return versions.get(app)