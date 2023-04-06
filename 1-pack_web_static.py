#!/usr/bin/python3
""" A Fabric script that generates a .tgz archive"""

from fabric.api import local
from datetime import datetime

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
    except:
        # return None if the archive has not been correctly generated
        return None

