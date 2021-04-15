#!/usr/bin/python3
"""
Fabric script that deletes out-of-date
archives, using the function do_clean
"""
from fabric.api import *


env.hosts = ['35.237.87.143', '35.237.66.227']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    if number == 0 or number == 1:
        local("cd versions")
        local("ls -1t | tail -n +2 | xargs rm -f")
        run("cd /data/web_static/releases")
        run("ls -1t | tail -n +2 | xargs rm -f")
    elif number >= 2:
        local("cd versions")
        local("ls -1t | tail -n +" + (number + 1) + " | xargs rm -f")
        run("cd /data/web_static/releases")
        run("ls -1t | tail -n +" + (number + 1) + " | xargs rm -f")
