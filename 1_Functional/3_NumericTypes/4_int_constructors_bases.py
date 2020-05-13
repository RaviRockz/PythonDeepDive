""""""

'''Constructors and Bases'''
''' 
    --> int(n, base=10)
        -> n = str, float
        -> base = [2, 8, 10, 16]
        
    --> Other Base To Int (Base 10)
        --> Base           Input                Output
             2         Binary  n = 0-1          Base 10
             8         Octal   n = 0-7          Base 10
            10         Decimal n = 0-9          Base 10
            16         Hex     n = 0-9 A-F      Base 10
             |
            36         Hex     n = 0-9 A-Z      Base 10
'''

print(int(5.6))  # float truncation
print(int('20'))
print(int(5))
print(int(-5))

print('Convert Other base to int')
print(int('1010', 2))
print(int('534', 8))
print(int('24', 10))
print(int('ff', 16))

print('Convert int to other base')
print(bin(10))
print(oct(348))
print(int(24))
print(hex(255))


class IntToOtherBase:
    def __init__(self, n, base=10):
        if base < 2:
            raise ValueError('Base must be >= 2')
        elif n < 0:
            raise ValueError('Number must be >= 0')
        else:
            import string
            self.n = n
            self.base = base
            self.digit_map = list(string.digits) + list(string.ascii_uppercase)
            self.digit_map = ''.join(self.digit_map[:base])

    def convert(self):
        if self.n == 0:
            return self.digit_map[0]
        else:
            digits = []
            while self.n > 0:
                self.n, m = divmod(self.n, self.base)
                digits.insert(0, m)
            if max(digits) >= len(self.digit_map):
                raise ValueError('invalid literal with base {0}: {1}'.format(self.base, self.n))
            return ''.join(self.digit_map[d] for d in digits)


class OtherBaseToInt:
    def __init__(self, n: str, base=10):
        if base < 2 or base > 36:
            raise ValueError('Invalid Base: 2 <= base <= 36')
        else:
            import string
            self.base = base
            self.digit_map = list(string.digits) + list(string.ascii_lowercase)
            self.n, self.sign = (n[1:], -1) if n[0] == '-' else (n, 1)

    def convert(self):
        result = 0
        for i, n in enumerate(self.n[::-1]):
            n = n.lower()
            result += self.digit_map.index(n) * self.base ** i
        if self.sign == -1:
            result = -1 * result
        return result


print('Convert int to other base Using Logic')
print(IntToOtherBase(10, 2).convert())
print(IntToOtherBase(348, 8).convert())
print(IntToOtherBase(24, 10).convert())
print(IntToOtherBase(255, 16).convert())

print('Convert other base to int Using Logic')
print(OtherBaseToInt('1010', 2).convert())
print(OtherBaseToInt('534', 8).convert())
print(OtherBaseToInt('24', 10).convert())
print(OtherBaseToInt('FF', 16).convert())
