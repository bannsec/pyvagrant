
import os
import logging
from .. import config

class Environments(object):
    def __init__(self, vagrant):
        self._vagrant = vagrant
        
        os.makedirs(self._environments_dir, exist_ok=True)

    def __repr__(self):
        return "<Environments " + str(len(self)) + ">"

    def __iter__(self):
        return self._environments.__iter__()

    def __len__(self):
        return len(self._environments)

    def __getitem__(self, item):
        if isinstance(item, str):
            try:
                return next(env for env in self._environments if env.name == item)
            except StopIteration:
                return None

        else:
            LOGGER.error("Unhandled getitem type of " + type(item))
    
    @property
    def _environments(self):
        _, envs, _ = next(os.walk(self._environments_dir))
        return [Environment(self._vagrant, name) for name in envs]

    @property
    def _environments_dir(self):
        return os.path.join(config.appdirs.user_data_dir, "environments")

from .environment import Environment

LOGGER = logging.getLogger(__name__)
