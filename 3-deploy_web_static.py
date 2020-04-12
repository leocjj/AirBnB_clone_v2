#!/usr/bin/python3
"""
script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy:
"""
from os.path import isfile
from fabric.api import *
from datetime import datetime

env.hosts = ['3.80.113.159', '104.196.66.20']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"
env.warn_only = True


def deploy():
    """ Create and distribute an archive to the web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

def do_pack():
    """ Generate a .tgz archive from the contents of the web_static folder """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_" + timestamp + ".tgz"
    local("mkdir -p versions")

    file_compresed = local("tar -cvzf " + file_path + " web_static")
    if file_compresed.failed:
        return None
    return file_path

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
