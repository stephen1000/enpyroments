import re
import unittest

from enpyronments.settings import Sensitive, Settings


class TestSettings(unittest.TestCase):
    def test_empty(self):
        """ Ensure an empty object doesn't error out (shouldn't be an issue, but makes me feel better) """
        settings = Settings()

    def test_masked__getitem__(self):
        """ Ensure accessing Settings elements via __getitem__ returns the underlying value when the key points to a
        Sensitive object"""
        val = "bet you cant see me!"
        sensitive = Sensitive(val)
        settings = Settings({"val": sensitive})

        self.assertEqual(settings.get("val"), val)

        masked_settings = settings.masked()
        self.assertNotEqual(masked_settings.get("val"), val)
        self.assertTrue(re.match(r"\*+", masked_settings.get("val")))

    def test_unmasked__getitem__(self):
        """ Ensure non-Sensitive objects are returned as a dict would """
