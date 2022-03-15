class MyComplex:
    def __init__(self, x, xj, xs='', xjs='+'):
        self.xs = '-' if xs == '' and x < 0 else xs
        self.x = x
        self.xjs = '-' if xj < 0 else xjs
        self.xj = xj
        sign = x != 0 or self.xs == '-'
        self.complex = f"{'(' if sign else ''}{self.xs}{abs(x) if sign else ''}" \
                       f"{self.xjs if sign else (self.xjs if self.xjs == '-' else '')}{abs(self.xj)}j" \
                       f"{')' if sign else ''}"

    def __add__(self, other):
        x = self.x + other.x
        xj = self.xj + other.xj
        return MyComplex(x, xj)

    def __mul__(self, other):
        x = self.x * other.x - self.xj * other.xj
        xj = self.x * other.xj + self.xj * other.x

        y = (1 if self.x == 0 else self.x) * (1 if other.x == 0 else other.x) - (1 if self.xj == 0 else self.xj) * (
            1 if other.xj == 0 else other.xj)
        yj = (1 if self.x == 0 else self.x) * (1 if other.xj == 0 else other.xj) + (1 if self.xj == 0 else self.xj) * (
            1 if other.x == 0 else other.x)

        xs = '-' if y < 0 else ''
        xjs = '-' if yj < 0 else '+'

        return MyComplex(x, xj, xs, xjs)

    def __str__(self):
        return self.complex


a = 5
aj = -1
b = 4
bj = -2

ac = MyComplex(a, aj)
bc = MyComplex(b, bj)
cc = ac * bc
dd = ac + bc

print('Complex mul')
print(f'MyClass print(obj)    -> {ac}*{bc}={cc}')
print(f'MyClass mul in print  -> {ac}*{bc}={ac * bc}')
print(f'Standard complex()    -> {complex(a, aj)}*{complex(b, bj)}={complex(a, aj) * complex(b, bj)}')

print()

print('Compex plus')
print(f'MyClass print(obj)    -> {ac}+{bc}={dd}')
print(f'MyClass plus in print -> {ac}+{bc}={ac + bc}')
print(f'Standard complex()    -> {complex(a, aj)}+{complex(b, bj)}={complex(a, aj) + complex(b, bj)}')
