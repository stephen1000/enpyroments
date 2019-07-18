import os
import sys
import unittest

from enpyronments import utils


class TestUtils(unittest.TestCase):

    def test_usepath(self):
        """ Find a path that isn't in sys.path already, and make sure that it
        is on sys.path within our context, and removed afterwards """
        
        new_path = 'i bet this isnt on your path'
        while new_path in sys.path:
            new_path = os.path.join('or maybe this isnt')

        # useless, but readable!
        self.assertNotIn(new_path, sys.path) 

        with utils.UsePath(new_path):
            self.assertIn(new_path, sys.path)

        self.assertNotIn(new_path, sys.path) 
