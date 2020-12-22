import subprocess


def get_calendar_string():
    return subprocess.check_output(["cal"]).decode()