# test_version.py
"""
Unit tests for `version.Version` class.
"""
import unittest
from version import Version


class TestVersion(unittest.TestCase):
    """Unit tests for `version.Version` class."""
    def test_str_method(self):
        self.assertEqual(str(Version('3.0.3')), '3.0.3')
        self.assertEqual(str(Version('3.1')), '3.1.0')
        self.assertEqual(str(Version('3')), '3.0.0')
    
    def test_repr_method(self):
        self.assertEqual(repr(v), "Version('3.0.3')")
    
    def test_number_of_digits(self):
        onedigit = Version('1')
        twodigits = Version('2.2')
        morethanthree = Version('1.2.3.4')
        self.assertEqual(v, Version('1.0.0'))
        self.assertEqual(v, Version('2.2.0'))
        with self.assertRaises(ValueError):
            Version('1.2.3.4')       
    
    def test_invalid_argument(self):
        with self.assertRaises(ValueError):
            Version('a')
        with self.assertRaises(ValueError):
            Version('nan')
        with self.assertRaises(ValueError):
            Version('')
        with self.assertRaises(AttributeError):
            Version(1.0)
        with self.assertRaises(Exception):
            Version(None)
    
    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Version()
        

if __name__ == "__main__":
    
    unittest.main()
    