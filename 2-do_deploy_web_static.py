#!/usr/bin/python3
"""
Module that distributes an archive to your web servers using function do_deploy
"""
from os.path import isfile
from fabric.api import *
from datetime import datetime


env.hosts = ['3.80.113.159', '104.196.66.20']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"
env.warn_only = True


def do_deploy(archive_path):
    """ Distribute an archive to the web servers """
    if not isfile(archive_path):
        return False
    try:
        # upload file to server
        put(archive_path, '/tmp/')

        archive = archive_path.replace('.tgz', '')
        archive = archive.replace('versions/', '')

        # create destination directory
        run("mkdir -p /data/web_static/releases/" + archive + "/")

        # uncompress tar file to a directory
        run("sudo tar -xzf /tmp/" + archive + ".tgz" +
            " -C /data/web_static/releases/" + archive + "/")

        # Delete file uploaded
        run("rm /tmp/" + archive + ".tgz")

        # move files to a previous folder
        run("mv /data/web_static/releases/" + archive +
            "/web_static/* /data/web_static/releases/" + archive + "/")

        # delete that folder
        run("rm -rf /data/web_static/releases/" + archive +
            "/web_static")

        # delete symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # create a new symbolic link
        run("ln -s /data/web_static/releases/" + archive +
            "/ /data/web_static/current")

        print("New version deployed!")
        return True
    except:
        return False
