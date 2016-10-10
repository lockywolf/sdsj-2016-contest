import unittest
from avellaneda2008 import library


class TestAvellaneda2008(unittest.TestCase):
    def setUp(self):
        pass

    def test_for_sanity(self):
        u"""
        Non-marked lines should only get 'p' tags around all input
        """
        self.assertTrue(
            library.FinMath.return_true,
            'basic')

if __name__ == '__main__':
    unittest.main()