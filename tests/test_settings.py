import re
import unittest

import pytest

from enpyronments.settings import Sensitive, Settings


class TestSettings(unittest.TestCase):
    """ Test case for the Settings class. Note that the settings dict here is always constructed from the pairs yielded
    by calling enumerate on one of self.values, self.sensitive_values, or self.all_values """
    
    def setUp(self):
        """ Provide a nice battery of types in values to test Settings """

        def func():
            """ Function type """

        self.values = [
            int(),
            float(),
            str(),
            bytes(),
            list(),
            dict(),
            set(),
            func,
            object(),
        ]
        self.sensitive_values = [Sensitive(value) for value in self.values]
        self.all_values = [*self.values, *self.sensitive_values]

    def test_empty(self):
        """ Ensure an empty object doesn't error out (shouldn't be an issue, but makes me feel better) """

        settings = Settings()
        return settings

    def test_masked(self):
        """ Ensure accessing Settings.masked() elements via __getitem__ returns the underlying value when the key points
         to a Sensitive object"""

        settings = Settings(enumerate(self.sensitive_values))

        for key, val in enumerate(self.values):
            self.assertEqual(settings[key], val)
            self.assertEqual(settings.get(key), val)

        masked_settings = settings.masked()
        for key, val in enumerate(self.values):
            # Make sure we didn't get back the masked value
            self.assertNotEqual(masked_settings.get(key), val)
            # Make sure we got back *'s instead
            self.assertTrue(re.match(r"\*+", masked_settings.get(key)))

    def assert__getitem__(self, settings):
        """ Asserts that __getitem__  returns the actual value of settings """
        for key, val in enumerate(self.values):
            setting = settings[key]
            self.assertEqual(setting, val)

    def test___getitem___masked(self):
        """ Ensure Sensitive objects return their underlying value """
        settings = Settings(enumerate(self.sensitive_values))
        self.assert__getitem__(settings)

    def test___getitem___unmasked(self):
        """ Ensure non-Sensitive objects are returned as a dict would """
        settings = Settings(enumerate(self.values))
        self.assert__getitem__(settings)
       

    def test___setitem___masked_defined(self):
        """ Ensure Sensitive objects when overwritten are still sensitive """
        old_settings = Settings(enumerate(self.sensitive_values))
        new_settings = dict(enumerate(self.sensitive_values))
        for key, value in new_settings.items():
            old_settings.__setitem__(key, value)
            self.assertIsInstance(old_settings.__getitem__(key, extract_from_sensitive=False), Sensitive)

    def test___setitem___masked_undefined(self):
        """ Ensure Sensitive objects return their underlying value """
        old_settings = Settings()
        new_settings = dict(enumerate(self.sensitive_values))
        for key, value in new_settings.items():
            old_settings.__setitem__(key, value)
            self.assertIsInstance(old_settings.__getitem__(key, extract_from_sensitive=False), Sensitive)

    def test___setitem___unmasked_defined(self):
        """ Ensure non-Sensitive objects are returned as a dict would """
        old_settings = Settings(enumerate(self.values))
        new_settings = dict(enumerate(self.sensitive_values))
        for key, value in new_settings.items():
            old_settings.__setitem__(key, value)
            self.assertIsInstance(old_settings.__getitem__(key, extract_from_sensitive=False), Sensitive)

    def test___setitem___unmasked_undefined(self):
        """ Ensure non-Sensitive objects are returned as a dict would """
        old_settings = Settings()
        new_settings = dict(enumerate(self.values))
        for key, value in new_settings.items():
            old_settings.__setitem__(key, value)
            self.assertNotIsInstance(old_settings.__getitem__(key, extract_from_sensitive=False), Sensitive)
