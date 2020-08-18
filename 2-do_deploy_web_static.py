#!/usr/bin/python3
"""script that generates a .tgz
"""
from fabric.api import put, env, run
from datetime import datetime
import os.path
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

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        filename = re.search('versions/(.*).tgz', archive_path)
        run('mkdir -p /data/web_static/releases/{}'.format(filename.group(1)))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'
            .format(filename.group(1), filename.group(1)))
        run('rm /tmp/{}.tgz'.format(filename.group(1)))
        run('mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'
            .format(filename.group(1), filename.group(1)))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(filename.group(1)))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(filename.group(1)))
        return True
    except:
        return False
