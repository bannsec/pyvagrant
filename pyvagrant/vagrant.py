import logging
import os
import shutil
import shelve
from . import config

class Vagrant(object):

    def __init__(self):
        self._config = shelve.open(os.path.join(config.appdirs.user_config_dir, "pyvagrant"), flag="c", writeback=True)
        self._prechecks()

    def _prechecks(self):
        
        if shutil.which("vagrant") is None:
            err = "Cannot find vagrant. Please install: https://www.vagrantup.com/downloads.html"
            LOGGER.error(err)
            raise Exception(err)

    def __repr__(self):
        return "<Vagrant v" + self.version + ">"

    def search(self, term, *args, **kwargs):
        return self.cloud.search(term, *args, **kwargs)

    @property
    def plugins(self):
        return Plugins(self)

    @property
    def cloud(self):
        return Cloud(self)

    @property
    def default_provider(self):
        try:
            return self._config['default_provider']
        except KeyError:
            self._config['default_provider'] = "virtualbox"
            return "virtualbox"

    @default_provider.setter
    def default_provider(self, default_provider):
        standard_providers = ["vmware_desktop", "virtualbox", "parallels", "libvirt" , "hyperv"]
        if default_provider not in standard_providers:
            LOGGER.warning("default_provider not in standard list {}. be sure you want to do this.".format(",".join(standard_providers)))

        self._config["default_provider"] = default_provider

    @property
    def boxes(self):
        """pyvagrant.box.Boxes: What boxes are installed?"""
        try:
            return self.__boxes
        except AttributeError:
            self.__boxes = Boxes(self)
            return self.__boxes

    @property
    def version(self):
        try:
            return self.__version
        except AttributeError:
            self.__version = subprocess.check_output(["vagrant", "-v"]).decode().split(" ")[-1].strip()
            return self.__version

    @property
    def environments(self):
        try:
            return self.__environments
        except AttributeError:
            self.__environments = Environments(self)
            return self.__environments


import subprocess
import re
from .plugins import Plugins
from .cloud import Cloud
from .box import Boxes
from .environments import Environments

LOGGER = logging.getLogger(__name__)
