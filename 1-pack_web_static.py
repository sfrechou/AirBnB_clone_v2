#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static folder
"""
from fabric.api import run
from fabric.api import local


def do_pack():
    """Generates a .tgz archive"""
    try:
        run("mkdir -p versions")
        n = datetime.now()
        filename = "versions/web_static_" + n.strftime("%Y%m%d%H%M%S") + ".tgz"
        local("tar -cvzf " + filename + " web_static")
        return filename
    except:
        return None
