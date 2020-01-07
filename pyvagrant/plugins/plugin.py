import logging

class Plugin(object):
    def __init__(self, name, version, scope):
        self.name = name
        self.version = version
        self.scope = scope

    def __repr__(self):
        return "<Plugin " + self.name + " " + self.version + ">"

LOGGER = logging.getLogger(__name__)
