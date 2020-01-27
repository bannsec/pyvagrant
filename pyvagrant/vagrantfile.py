
import logging
import os
import pickle
import atexit

class Vagrantfile:
    def __init__(self, environment, provider=None):
        """Represents a Vagrantfile.

        Args:
            environment (pyvagrant.environments.Environment): The environment
                to for this Vagrantfile.
            provider (str, optional): What provider to use. Defaults to the
                default provider.
        """
        self._environment = environment
        self._provider = provider or self._environment._vagrant.default_provider
        self.boxes = {}
        atexit.register(self._sync)

    def add_box(self, box, name=None):
        """Adds a box to this vagrantfile and give's it the name.

        Args:
            box (pyvagrant.box.Box): Box to add
            name (str, optional): What to name it (default is 'default')
        """

        if not isinstance(box, Box):
            LOGGER.error("Must add Box type to Vagrantfile. Got type: " + str(type(box_)))
            return

        if not name: name = "default"
        self.boxes[name] = {
            'box': box,
            'options': BoxOptions(vagrant=self._environment._vagrant, provider=self._provider),
        }

    def __str__(self):
        out = VAGRANTFILE_BASE

        config = ""
        for name, box in self.boxes.items():
            config += 'config.vm.define "{name}" do |box|\n'.format(name=name)
            config += 'box.vm.box   = ' + box['box'].name + '\n'
            # Box config
            config += 'end\n'

        return VAGRANTFILE_BASE.format(config=config)

    def _sync(self):
        """Sync's the current object to it's pickle file."""
        with open(self._environment._vagrantfile_pickle_path, "wb") as f:
            pickle.dump(self, f)

    def __repr__(self):
        return "<Vagrantfile " + self._environment.name + ">"

    # For pickling issues
    def __getstate__(self):
        return {'_provider': self._provider, 'boxes': self.boxes}

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Make sure we sync at exit
        atexit.register(self._sync)

from .box import Box, BoxOptions

LOGGER = logging.getLogger(__name__)

VAGRANTFILE_BASE = r"""Vagrant.configure("2") do |config|
{config}
end"""
