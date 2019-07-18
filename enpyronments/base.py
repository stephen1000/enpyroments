import os

from enpyronments.utils import Sensitive


class Settings(dict):
    """Holder object for settings."""

    def masked(self):
        return dict(zip(self.keys(), (v.mask() if isinstance(v, Sensitive) else v for v in self.values())))

    def __getitem__(self, key):
        """ same as dict.__getitem__, but extracts the value of Sensitive type elements """
        val = super().__getitem__(key)
        if isinstance(val, Sensitive):
            return val.obj
        return val

    def __setitem__(self, key, val):
        """ Same as dict.__setitem__, but sets the value of Sensitive type elements if the current value is already
        Sensitive """
        if key in self and isinstance(self[key], Sensitive):
            return super().__setitem__(key, Sensitive(val))
        return super().__setitem__(key, val)

    def get(self, key, default=None):
        """ Same as dict.get, but extracts the value of Sensitive type elements """
        try:
            val = self[key]
        except KeyError:
            return default

        if isinstance(val, Sensitive):
            return val.obj

        return val

    def items(self):
        """ Same as dict.items, but extracts the value of Sensitive type elements """
        for key, val in super().items():
            if isinstance(val, Sensitive):
                yield key, val.obj
            yield key, val

    def values(self):
        """ Same as dict.values, but extracts the value of Sensitive type elements """
        for val in super().values():
            if isinstance(val, Sensitive):
                yield val.obj
            yield val

    def save_to_environ(self):
        """Saves the current state of settings to the environment via os.environ"""
        os.environ.update(self)
