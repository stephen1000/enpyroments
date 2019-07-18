import os

from enpyronments.utils import Sensitive


class Settings(dict):
    """Holder object for settings."""

    def masked(self):
        return dict(zip(self.keys(), (v.mask() if isinstance(v, Sensitive) else v for v in self.values())))

    def __getitem__(self, key):
        val = super().__getitem__(key)
        if isinstance(val, Sensitive):
            return val.obj
        return val

    def get(self, key, default=None):
        """ Same as dict.get, but extracts the value of Sensitive type elements """
        try:
            val = self[key]
        except KeyError:
            return default

        if isinstance(val, Sensitive):
            return val.obj

        return val
        

    def save_to_environ(self):
        """Saves the current state of settings to the environment via os.environ"""
        os.environ.update(self)
