# router.py

from tools import (
    check_server_status,
    check_database_status,
    get_application_version,
    get_cpu_usage,
    get_disk_space
)

TOOLS = {
    "check_server_status": check_server_status,
    "check_database_status": check_database_status,
    "get_cpu_usage": get_cpu_usage,
    "get_disk_space": get_disk_space,
    "get_application_version": get_application_version
}