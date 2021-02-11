import os
import pathlib
from minerl.data.util.constants import touch

MODULE_PATH = pathlib.Path(__file__).parent.absolute()
BLACKLIST_DIR_PATH = MODULE_PATH / 'assets' / 'blacklist'


class Blacklist:

    def __init__(self, blacklist_dir=BLACKLIST_DIR_PATH):
        self.blacklist_dir = blacklist_dir
        os.makedirs(self.blacklist_dir, exist_ok=True)

    def add(self, entry):
        touch(self.blacklist_dir / entry)

    def __contains__(self, item):
        return item in os.listdir(self.blacklist_dir)
