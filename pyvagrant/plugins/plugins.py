import logging
import subprocess
import re

class Plugins(object):

    def __init__(self, vagrant):
        self._vagrant = vagrant
        self._update()

    def uninstall(self, plugin):

        if isinstance(plugin, Plugin):
            plugin = plugin.name

        subprocess.check_output(["vagrant", "plugin", "uninstall", plugin])
        self._update()

    def install(self, plugin):

        subprocess.check_output(["vagrant", "plugin", "install", plugin])
        self._update()

    def _update(self):
        self._plugins = []
        plugins = subprocess.check_output(["vagrant", "plugin", "list"])

        for name, version, scope in re.findall(b"^(.+?) +\((.+?), +(.+?)\)", plugins):
            self._plugins.append(Plugin(name.decode(), version.decode(), scope.decode()))

    def __repr__(self):
        return "<Plugins " + str(len(self)) + ">"

    def __iter__(self):
        return self._plugins.__iter__()

    def __len__(self):
        return len(self._plugins)

from .plugin import Plugin
LOGGER = logging.getLogger(__name__)
