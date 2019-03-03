'''
import unittest
from tasks.cryptography import encrypt_this


class Test(unittest.TestCase):
    def for_another_strig(self):
        self.assertEqual(encrypt_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
                         ['6', '1', '1', '1', '1', '1', '9', '1'])


if __name__ == '__main__':
    unittest.main()

'''