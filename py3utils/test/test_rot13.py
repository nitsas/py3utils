#!/usr/bin/env python3


import string
import unittest
# modules I've written:
from ..rot13 import rot13


class Rot13TestCase(unittest.TestCase):
    """
    Test the rot13 function.
    
    It should convert any ASCII English letter chars in the given string to
    ROT13 and back.
    """
    
    def setUp(self):
        self.ascii_letters = string.ascii_letters
        self.ascii_letters_rot13 = string.ascii_lowercase[13:] + \
                                   string.ascii_lowercase[:13] + \
                                   string.ascii_uppercase[13:] + \
                                   string.ascii_uppercase[:13]
    
    def test_converts_to_rot13_correctly(self):
        self.assertEqual(self.ascii_letters_rot13, rot13(self.ascii_letters))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
