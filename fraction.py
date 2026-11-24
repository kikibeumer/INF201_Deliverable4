import math

class Fraction:
    """Represent fractions"""
    
    def __init__(self, numerator: int, denominator: int) -> None:
        # Check that numerator and denominator are integers, and that denominator is >0
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        if denominator <= 0:
            raise ValueError("Denominator must be strictly positive")

        self.n = numerator
        self.d = denominator
    
    def _cross_multiply(self, other: "Fraction") -> tuple[int]:
        """Cross multiply fractions for easier comparison and calculations"""
        a = self.n * other.d
        b = other.n * self.d
        return a, b
    
    # -------- Comparison methods --------
    
    def __eq__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        a, b = self._cross_multiply(other)
        return a == b
    
    def __ne__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        a, b = self._cross_multiply(other)
        return a != b
        
    def __lt__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        a, b = self._cross_multiply(other)
        return a < b
        
    def __le__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        a, b = self._cross_multiply(other)
        return a <= b
        
    def __gt__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        a, b = self._cross_multiply(other)
        return a > b
    
    def __ge__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        a, b = self._cross_multiply(other)
        return a >= b
    

    # -------- Arithmetic methods --------
    
    def __add__(self, other: "Fraction"):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Cross-multiply 
        a, b = self._cross_multiply(other)
        # Add nominators and multiply denominators
        sum_n = a + b
        sum_d = self.d * other.d
        # Reduce to lowest by dividing by greatest common divisor
        g = math.gcd(sum_n, sum_d)
        sum_n = sum_n // g # Double slash for integer division
        sum_d = sum_d // g
        return sum_n, sum_d
    
    def __sub__(self, other: "Fraction"):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Cross-multiply 
        a, b = self._cross_multiply(other)
        # Subtract nominators and multiply denominators
        diff_n = a - b
        diff_d = self.d * other.d
        # Reduce to lowest by dividing by greatest common divisor
        g = math.gcd(diff_n, diff_d)
        diff_n = diff_n // g # Double slash for integer division
        diff_d = diff_d // g
        return diff_n, diff_d
    
    def __mul__(self, other: "Fraction"):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Multiply nominators and multiply denominators
        prod_n = self.n * other.n
        prod_d = self.d * other.d
        # Reduce to lowest by dividing by greatest common divisor
        g = math.gcd(prod_n, prod_d)
        prod_n = prod_n // g # Double slash for integer division
        prod_d = prod_d // g
        return prod_n, prod_d
    
    def __truediv__(self, other: "Fraction"):
            if not isinstance(other, Fraction):
                return NotImplemented
            # Check for zero-division
            if other.n == 0:
                raise ZeroDivisionError
            # Cross multiply
            quo_n = self.n * other.d
            quo_d = self.d * other.n
            # Reduce to lowest by dividing by greatest common divisor
            g = math.gcd(quo_n, quo_d)
            quo_n = quo_n // g # Double slash for integer division
            quo_d = quo_d // g
            return quo_n, quo_d

