
import shutil
import os

class Environment(object):
    def __init__(self, vagrant, name):
        self._vagrant = vagrant
        self.name = name

    def remove(self):
        shutil.rmtree(self._path)

    def __repr__(self):
        return "<Environment " + self.name + ">"

    @property
    def _path(self):
        return os.path.join(self._vagrant.environments._environments_dir, self.name)
