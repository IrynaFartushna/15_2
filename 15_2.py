class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b

    def __mul__(self, other):
        """Multiply two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other):
        """Add two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        """Subtract two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        """Check equality of two fractions."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b == self.b * other.a

    def __ne__(self, other):
        """Check inequality of two fractions."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Check if the first fraction is less than the second."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        """Check if the first fraction is greater than the second."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b > self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(str(f_c))
f_d = f_b * f_a
print(str(f_d))
f_e = f_a - f_b
print(str(f_e))

print(f_d < f_c)
print(f_d > f_e)
print(f_a != f_b)
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
print(f_1 == f_2)
print('OK')



