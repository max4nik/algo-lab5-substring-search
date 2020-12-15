import unittest

from main.main import main


class KMPTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual([(0, 3), (9, 12)], main('test1'))

    def test_2(self):
        self.assertEqual([(0, 0), (1, 1), (2, 2)], main('test2'))

    def test_3(self):
        with self.assertRaises(SystemExit):
            main('test3')

    def test_4(self):
        self.assertEqual([(0, 3), (3, 6)], main('test4'))


if __name__ == '__main__':
    unittest.main()
