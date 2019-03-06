import unittest
from tasks.cryptography import encrypt_this


class Test(unittest.TestCase):
    def for_another_strig(self):
        self.assertEqual(encrypt_this('Hello'), '72olle')


if __name__ == '__main__':
    unittest.main()
