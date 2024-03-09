#!/usr/bin/python3
"""
Clean all archives based on the number of
arguements passed
"""
import os
from fabric.api import *

env.hosts = ["34.207.222.225", "100.25.2.85"]
env.user = "ubuntu"


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives, including most recent to keep.
    Desc:
        If number is 0 or 1, keep only the most recent archive. If
        number is 2, keeps the most and second-most recent archives,
        etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local(f"rm ./{archive}") for archive in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run(f"rm -rf ./{a}") for archive in archives]
