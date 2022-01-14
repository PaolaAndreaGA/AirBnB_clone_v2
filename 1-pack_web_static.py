#!/usr/bin/python3
# module that holds method that generates a .tgz archive

from fabric.api import local
import datetime


def do_pack():
    """ Generates a .tgz archive """
    local("mkdir -p versions")
    t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive = local("tar -czvf versions/web_static_{}\
.tgz web_static".format(t))
    if archive:
        return ("versions/web_static_{}".format(t))
    else:
        return None
