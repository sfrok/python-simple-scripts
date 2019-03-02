import unittest
from tasks.simple_task import square


class Test(unittest.TestCase):
    def add_str(self):
        self.assertEqual(square('10'), (40, 100, 14.142135623730951))

    def add_random_symbol(self):
        self.assertEqual(square('abc'), 'Please check you input statement')


if __name__ == '__main__':
    unittest.main()
