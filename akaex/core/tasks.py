from base.celery import app


import os
import subprocess
from datetime import datetime
from os import path

from django.conf import settings
from django.core.management import call_command


@app.task(bind=True)
def create_sqlite_backup(self):

    ROOT_DIR = os.getcwd()

    BACKUPS_DIR = f"{ROOT_DIR}/dabase-backups"

    if not path.exists(BACKUPS_DIR) :
        os.makedirs(BACKUPS_DIR)

    now = datetime.now()  # current date and time
    date_time_now = now.strftime("%Y-%m-%d_%H-%M-%S")

    cmd_str = f"python {ROOT_DIR}/manage.py dumpdata > ./dabase-backups/backup-db_{date_time_now}.json"

    # Create Database backup
    execute_command(cmd_str)


def execute_command(cmd=None):

    if isinstance(cmd, str):
        returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
        #print('returned value:', returned_value)



@app.task(bind=True)
def backup(self):
    if settings.DEBUG is True:
        return f"Could not be backed up: Debug is True"
    else:
        try:
            call_command("dbbackup", "--clean")
            return f"Backed up successfully: {datetime.now()}"
        except:
            return f"Could not be backed up: {datetime.now()}"


@app.task(bind=True)
def mediabackup(self):
    if settings.DEBUG is True:
        return f"Could not be backed up: Debug is True"
    else:
        try:
            call_command("mediabackup", "--clean")
            return f"Backed up successfully: {datetime.now()}"
        except:
            return f"Could not be backed up: {datetime.now()}"