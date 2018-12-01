import unittest
from cython_test_coverage.basic_cython import add_test_cython


class TestMethods(unittest.TestCase):
     def test_func(self):
          self.assertEqual(add_test_cython(2,3), 5)

if __name__ == '__main__':
     unittest.main()
