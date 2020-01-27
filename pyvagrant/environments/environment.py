
import shutil
import os
import pickle

class Environment(object):
    def __init__(self, vagrant, name):
        self._vagrant = vagrant
        self.name = name

        os.makedirs(self._path, exist_ok=True)

    def remove(self):
        shutil.rmtree(self._path)

    def __repr__(self):
        return "<Environment " + self.name + ">"

    @property
    def _vagrantfile(self):
        try:
            return self.__vagrantfile
        except AttributeError:
            # Load existing Vagrantfile
            if os.path.isfile(self._vagrantfile_pickle_path):
                with open(self._vagrantfile_pickle_path, "rb") as f:
                    self.__vagrantfile = pickle.load(f)
                    self.__vagrantfile._environment = self
            else:
                # Start up new one
                self.__vagrantfile = Vagrantfile(self)
            return self.__vagrantfile

    @property
    def _vagrantfile_pickle_path(self):
        return os.path.join(self._path, "Vagrantfile.pickle")

    @property
    def _path(self):
        return os.path.join(self._vagrant.environments._environments_dir, self.name)

from ..vagrantfile import Vagrantfile
