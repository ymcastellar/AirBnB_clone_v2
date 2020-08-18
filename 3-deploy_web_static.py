#!/usr/bin/python3
"""script that generates a .tgz
"""
from fabric.api import put, env, run, local
from datetime import datetime
from os.path import exists, isdir
import re

env.hosts = ['35.231.14.75', '54.242.226.110']


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


def do_deploy(archive_path):
    """that distributes an archive to your web servers
    """

    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """Compress files in .tgz"""
    pack = do_pack()
    if pack is None:
        return False
    dep = do_deploy(pack)
    return dep
