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

    try:
        # Upload archive to web servers
        put(archive_path, '/tmp/')

        # Create directory to uncompress archive
        run(f'mkdir -p /data/web_static/releases/{archive_dir}/')

        # Uncompress archive to directory
        run(f'tar -xzf /tmp/{archive_name} \
             -C /data/web_static/releases/{archive_dir}/')

        # Remove archive from web servers
        run(f'rm /tmp/{archive_name}')

        # Delete symbolic link to current code
        run('rm -f /data/web_static/current')

        # Create new symbolic link to new version of code
        run(f'ln -s /data/web_static/releases/{archive_dir}/ \
             /data/web_static/current')

        print(f"New version of code successfully deployed to web servers.")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

