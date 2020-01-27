
class BoxOptions:
    def __init__(self, vagrant, provider=None):
        self._vagrant = vagrant
        self._provider = provider or self._vagrant.default_provider
        self._options = {}

    def __getstate__(self):
        return {'_options': self._options, '_provider': self._provider}
