#!/usr/bin/python3
"""
Fabric script that archives <'web_static'> and deploys it to my web servers
"""

import os
from fabric.api import env, put, run, local
from datetime import datetime

# Set Fabric environment variables
env.hosts = ['34.229.72.112', '100.27.3.239']
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa.pub'


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        local("mkdir -p versions")
        current_date = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "web_static_" + current_date + ".tgz"
        local("tar -cvzf versions/{} web_static".format(filename))
        return "versions/{}".format(filename)
    except None:
        # return None if the archive has not been correctly generated
        return None


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


def deploy():
    """Compresses and distributes archive to web servers for full deployment"""
    compress_archive = do_pack()
    if not compress_archive:
        return False

    return do_deploy(compress_archive)
