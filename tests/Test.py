import unittest

from solution.kmp import kmp_search


class KMPTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(True, kmp_search('Hello World!', 'ello'))

    def test_2(self):
        self.assertEqual(True, kmp_search('Test 2', '2'))

    def test_3(self):
        self.assertEqual(False, kmp_search('Nothing', 'something'))

    def test_4(self):
        self.assertEqual(True, kmp_search('self.assertEqual(True, kmp_search(''))', 'assert'))


if __name__ == '__main__':
    unittest.main()
