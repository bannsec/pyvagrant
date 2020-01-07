import logging
import os
import shutil

class Vagrant(object):

    def __init__(self):
        self._prechecks()

    def _prechecks(self):
        
        if shutil.which("vagrant") is None:
            err = "Cannot find vagrant. Please install: https://www.vagrantup.com/downloads.html"
            LOGGER.error(err)
            raise Exception(err)

    def search(self, term):
        return self.cloud.search(term)

    @property
    def plugins(self):
        return Plugins(self)

    @property
    def cloud(self):
        return Cloud(self)

    @property
    def default_provider(self):
        return "virtualbox"

    @property
    def boxes(self):
        """list: What boxes are installed?"""
        output = subprocess.check_output(["vagrant", "box", "list"])
        boxes = []
        for name, provider, version in re.findall(b"^(.+?) +\((.+?), +(.+?)\)", output):
            boxes.append(Box(self, name.decode(), version.decode(), providers=provider.decode()))

        return boxes


import subprocess
import re
from .plugins import Plugins
from .cloud import Cloud
from .box import Box

LOGGER = logging.getLogger(__name__)
