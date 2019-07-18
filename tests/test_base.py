import re
import unittest

from enpyronments.base import Sensitive, Settings


class TestSettings(unittest.TestCase):
    def test_empty(self):
        settings = Settings()

    def test_masking(self):
        val = "bet you cant see me!"
        sensitive = Sensitive(val)
        settings = Settings({"val": sensitive})

        self.assertEqual(settings.get("val"), val)

        masked_settings = settings.masked()
        self.assertNotEqual(masked_settings.get("val"), val)
        self.assertTrue(re.match(r"\*+", masked_settings.get("val")))
