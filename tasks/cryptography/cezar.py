class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, str):
        s = str.upper()
        s1 = ''
        for c in s:
            if ord(c) > 90 or ord(c) < 65:
                s1 += c
                continue
            a = ord(c) + self.shift
            s1 += chr(a - 26) if a > 90 else chr(a)
        return s1

    def decode(self, str):
        s1 = ''
        for c in str:
            if ord(c) > 90 or ord(c) < 65:
                s1 += c
                continue
            a = ord(c) - self.shift
            s1 += chr(a + 26) if a < 65 else chr(a)
        return s1


c = CaesarCipher(5)
print(c.encode('Hello'))
print(c.decode('MJQQT'))

