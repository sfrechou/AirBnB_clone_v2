#!/usr/bin/python3
"""
Fabric script that creates and distributes an
archive to your web servers, using the function deploy
"""
from datetime import datetime
import os
from fabric.api import *


env.hosts = ['35.237.87.143', '35.237.66.227']


def do_pack():
    """Generates a .tgz archive"""
    try:
        local("mkdir -p versions")
        n = datetime.now()
        filename = "versions/web_static_" + n.strftime("%Y%m%d%H%M%S") + ".tgz"
        local("tar -cvzf " + filename + " web_static")
        return filename
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            filename = archive_path.split('/', 1)
            no_ext = filename[1].split('.', 1)
            archive = no_ext[0]
            run("mkdir -p /data/web_static/releases/" + archive + "/")
            run("tar -zxf /tmp/" + filename[1] +
                " -C /data/web_static/releases/" +
                archive + "/")
            run("rm /tmp/" + filename[1])
            run("mv /data/web_static/releases/" + archive +
                "/web_static/* /data/web_static/releases/" + archive + "/")
            run("rm -rf /data/web_static/releases/" + archive + "/web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/" + archive +
                "/ /data/web_static/current")
            print("New version deployed!")
            return True
        except:
            return False
    else:
        return False


def deploy():
    """Creates and distributes an archive to your web servers"""
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
