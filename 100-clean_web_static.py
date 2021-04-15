#!/usr/bin/python3
"""
Fabric script that deletes out-of-date
archives, using the function do_clean
"""
from fabric.api import *


env.hosts = ['35.237.87.143', '35.237.66.227']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    num = int(num)
    if num == 0 or num == 1:
        local("cd versions; ls -t | tail -n +2 | xargs rm -f")
        run("cd /data/web_static/releases; ls -t | tail -n +2 | xargs rm -f")
    elif num >= 2:
        num += 1
        local("cd versions; ls -t | tail -n +{} | xargs rm -f".format(num))
        run("cd /data/web_static/releases; ls -t | tail -n +{} | xargs rm -f".format(num))
