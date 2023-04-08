#!/usr/bin/python3
"""
Fabric script to distribute archive to web servers using do_deploy function.
"""

import os
from fabric.api import env, put, run, local

# Set Fabric environment variables
env.hosts = ['34.229.72.112', '100.27.3.239']
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa.pub'


def do_deploy(archive_path):
    """Distributes an archive to web servers using Fabric."""

    # Check if archive exists
    if not os.path.exists(archive_path):
        print(f"Archive file {archive_path} does not exist")
        return False

    # Define variables
    archive_name = os.path.basename(archive_path)
    archive_dir = os.path.splitext(archive_name)[0]
    folder_path = "/data/web_static/releases/"

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}".format(folder_path, archive_dir))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, folder_path))
        run("rm -rf /tmp/{}".format(archive_name))
        run("mv {}web_static/* {}{}".format(folder_path, folder_path, archive_dir))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(folder_path, archive_dir))
        print('New version deployed!')
        success = True

        print(f"New version of code successfully deployed to web servers.")
        return success

    except Exception as e:
        print(f"Error: {e}")
        return False
