
import logging
import subprocess

class Box(object):
    def __init__(self, vagrant, name, version, downloads=None, providers=None):
        self._vagrant = vagrant
        self.name = name
        self.version = version
        self.downloads = downloads
        self.providers = providers

    def add(self):
        """Downloads the box."""
        subprocess.check_output(["vagrant", "box", "add", "-c", "--box-version", self.version, "--provider", self._vagrant.default_provider, self.name])

    def remove(self):
        """Remove this box."""
        subprocess.check_output(["vagrant", "box", "remove", self.name])

    def __repr__(self):
        return "<Box " + self.name + " " + self.version + " " + ",".join(self.providers) + ">"

    def __getstate__(self):
        return {'name': self.name, 'version': self.version, 'downloads': self.downloads, 'providers': self.providers}

    @property
    def providers(self):
        return self.__providers

    @providers.setter
    def providers(self, providers):
        if isinstance(providers, str):
            providers = providers.split(",")

        elif isinstance(providers, bytes):
            providers = providers.split(b",")

        self.__providers = providers

    @property
    def downloads(self):
        return self.__downloads

    @downloads.setter
    def downloads(self, downloads):
        if isinstance(downloads, str):
            downloads = int(downloads.replace(",",""), 10)

        elif isinstance(downloads, bytes):
            downloads = int(downloads.replace(b",",""), 10)

        self.__downloads = downloads

LOGGER = logging.getLogger(__name__)
