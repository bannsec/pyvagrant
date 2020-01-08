import logging

class ProviderBase(object):
    def __init__(self, vagrant):
        self._vagrant = vagrant

LOGGER = logging.getLogger(__name__)
