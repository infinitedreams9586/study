class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real_component = int(real) if isinstance(real, int) else float(real)
        self.imaginary_component = int(imaginary) if isinstance(imaginary, int) else float(imaginary)

    def __repr__(self):
        return "{real}{sign}{imaginary}{i}".format(real=self.real_component,
                                                 sign='+' if self.imaginary_component > 0 else '',
                                                 imaginary= '' if self.imaginary_component in [0, 1] else self.imaginary_component,
                                                 i = 'i' if self.imaginary_component != 0 else '')

    def __add__(self, other):
        if not self._is_complex_number(other):
            return
        real_add = self.real_component + other.real_component
        imaginary_add = self.imaginary_component + other.imaginary_component
        return ComplexNumber(real_add, imaginary_add)

    def __sub__(self, other):
        if not self._is_complex_number(other):
            return
        real_sub = self.real_component - other.real_component
        imaginary_sub = self.imaginary_component - other.imaginary_component
        return ComplexNumber(real_sub, imaginary_sub)

    def __mul__(self, other):
        if not self._is_complex_number(other):
            return
        # self: (a1, b1) where a is real component, and b is imaginary component
        # other: (a2, b2) where a is real component, and b is imaginary component
        a1a2 = self.real_component * other.real_component
        b1b2 = self.imaginary_component * other.imaginary_component
        a1b2 = self.real_component * other.imaginary_component
        a2b1 = self.imaginary_component * other.real_component

        return ComplexNumber(a1a2 - b1b2, a1b2 + a2b1)

    def __div__(self, other):
        if not self._is_complex_number(other):
            return
        # self: (a1, b1) where a is real component, and b is imaginary component
        # other: (a2, b2) where a is real component, and b is imaginary component
        a1a2 = self.real_component * other.real_component
        b1b2 = self.imaginary_component * other.imaginary_component
        a1b2 = self.real_component * other.imaginary_component
        a2b1 = self.imaginary_component * other.real_component
        a2_squared = other.real_component ** 2
        b2_squared = other.imaginary_component ** 2

        return ComplexNumber((a1a2 + b1b2) / (a2_squared + b2_squared), (a2b1 - a1b2) / (a2_squared + b2_squared))

    def modulus(self):
        import math
        return math.sqrt(self.real_component ** 2 + self.imaginary_component ** 2)

    def conjugate(self):
        other = ComplexNumber(self.real_component, (-1) * self.imaginary_component)
        return self.__mul__(other)

    def _is_complex_number(self, other):
        if not isinstance(other, ComplexNumber):
            print("Invalid complex number.")
            return False
        return True


if __name__ == '__main__':
    c1 = ComplexNumber(3, 2)
    c2 = ComplexNumber(-1, -1)
    print(c1)
    print(c2)

    print("Sum:", c1+c2)
    print("Subtraction:", c1-c2)
    print("Multiplication:", c1*c2)
    print("Division:", c1/c2)
    print("Modulus:", c1.modulus())
    print("Conjugate:", c1.conjugate())