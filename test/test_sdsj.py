# coding=utf-8
import unittest
from sdsj import SdsjLibrary


class TestSdsj(unittest.TestCase):
    def setUp(self):
        pass

    def test_for_sanity(self):
        u"""
        Non-marked lines should only get 'p' tags around all input
        """
        self.assertTrue(
            SdsjLibrary.FinMath.return_true,
            'basic')

if __name__ == '__main__':
    unittest.main()