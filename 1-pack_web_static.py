#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the a folder"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ a function that clones the repo and pack contents  into archive.tgz """

    local("mkdir -p versions")
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    file = f"versions/web_static_{timestamp}.tgz"
    result = local(f"tar -cvzf {file} web_static", capture=True)
    return file
