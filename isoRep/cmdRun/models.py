# Database import

from django import db

# Settings import
from django.conf import settings

# Other import
from datetime import datetime


def command_run_db(name, command, status,log_file):
    date = datetime.now()

    items = {
        "Sdate": date,
        "Fdate": None,
        "File": log_file,
        "Name": name,
        "Command": command,
        "Status": None
    }

    process_id = db.new_task(command)

    if status == 0:
        db.update_task(process_id, "Sdate", items["Sdate"])
        db.update_task(process_id, "Fdate", datetime.now())
        db.update_task(process_id, "File", items["File"])
        db.update_task(process_id, "Name", items["Name"])
        db.update_task(process_id, "Command", items["Command"])
        db.update_task(process_id, "Status", status)
    else:
        db.update_task(process_id, "Sdate", items["Sdate"])
        db.update_task(process_id, "Fdate", datetime.now())
        db.update_task(process_id, "File", items["File"])
        db.update_task(process_id, "Name", items["Name"])
        db.update_task(process_id, "Command", items["Command"])
        db.update_task(process_id, "Status", status)
