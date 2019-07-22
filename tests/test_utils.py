import os
import re
import sys
import unittest

from enpyronments import utils


class TestUsePath(unittest.TestCase):

    def test_usepath(self):
        """ Find a path that isn't in sys.path already, and make sure that it
        is on sys.path within our context, and removed afterwards """

        new_path = "i bet this isnt on your path"
        while new_path in sys.path:
            new_path = os.path.join("or maybe this isnt")

        # useless, but readable!
        self.assertNotIn(new_path, sys.path)

        with utils.UsePath(new_path):
            self.assertIn(new_path, sys.path)

        self.assertNotIn(new_path, sys.path)


class TestSensitive(unittest.TestCase):
    def setUp(self):
        """ Sample of different types to test """
        self.vals = [
            int(),
            float(),
            str(),
            bytes(),
            list(),
            dict(),
            object(),
        ]

    def test_sensitive(self):
        """ Ensure sensitive's obj attribute is loaded with our value """
        for val in self.vals:
            sensitive = utils.Sensitive(val)
            self.assertEqual(sensitive.obj, val)

    def test_sensitive_no_stars(self):
        """ Ensure AttributeError is raised when stars <= 0 """
        with self.assertRaises(AttributeError):
            utils.Sensitive('foo', stars=0)

    def test_sensitive_mask(self):
        """ Ensure the mask method returns only asterisks """
        for val in self.vals:
            sensitive = utils.Sensitive(val)
            self.assertTrue(re.match(r'\*+', sensitive.mask()))

    def test_sensitive_str(self):
        """ Ensure that str(Sensitive) is the same as str(val) """
        for val in self.vals:
            sensitive = utils.Sensitive(val)
            self.assertEqual(str(sensitive), str(val))
            
    def test_sensitive_repr(self):
        """ Ensure that repr(Sensitive) doesn't raise errors """
        for val in self.vals:
            sensitive = utils.Sensitive(val)
            repr(sensitive)
