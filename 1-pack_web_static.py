#!/usr/bin/python3
"""
Module that contain a script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generate a .tgz archive from the contents of the web_static folder """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_" + timestamp + ".tgz"
    local("mkdir -p versions")

    file_compresed = local("tar -cvzf " + file_path + " web_static")
    if file_compresed.failed:
        return None
    return file_path
