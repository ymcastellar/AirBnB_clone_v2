#!/usr/bin/python3
"""script that generates a .tgz
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Compress files in .tgz"""

    local("mkdir -p versions")
    time = datetime.now()
    date = time.strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_" + date
    file = local("tar -cvzf {}.tgz web_static".format(path))
    if file.succeeded:
        return (path)
    else:
        return (None)
