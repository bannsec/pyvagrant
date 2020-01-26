
import logging
import re
import subprocess
from prettytable import PrettyTable
import fnmatch

class Boxes:
    def __init__(self, vagrant):
        self._vagrant = vagrant

    def __repr__(self):
        count = len(self)
        attrs = ["Boxes", str(count), "box" if count == 1 else "boxes"]
        return "<" + " ".join(attrs) + ">"

    def __iter__(self):
        return self._boxes.__iter__()

    def __len__(self):
        return len(self._boxes)

    def __str__(self):
        table = PrettyTable(["Name", "Version", "Providers"])
        table.align = "l"

        for box in self:
            table.add_row([box.name, box.version, ",".join(box.providers)])

        return str(table)

    def __getitem__(self, item):

        if isinstance(item, int):
            return list(self._boxes)[item]

        elif isinstance(item, str):
            try:
                return next(box for box in self if fnmatch.fnmatch(box.name, item))
            except StopIteration:
                LOGGER.error("Couldn't find box with that name. Did you download it?")
                return
        
        else:
            LOGGER.error("Unhandled getitem of type " + str(type(item)))

    @property
    def _boxes(self):
        """list: List of boxes."""
        output = subprocess.check_output(["vagrant", "box", "list"])
        boxes = []
        for name, provider, version in re.findall(b"(.+?) +\((.+?), +(.+?)\)", output):
            boxes.append(Box(self, name.decode(), version.decode(), providers=provider.decode()))

        return boxes

from .box import Box

LOGGER = logging.getLogger(__name__)
