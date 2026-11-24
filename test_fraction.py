from fraction import Fraction

def test_fraction():
    """
    Test all special methods of class Fraction
    """
    a = Fraction(1, 2)
    b = Fraction(2, 4)
    c = Fraction(3, 4)
    
    # __eq__()
    assert a == b 
    assert not a == c
    
    # __ne__()
    assert b != c
    assert not b != a
    
    # __gt__()
    assert c > b
    assert not a > b
    
    # __ge__()
    assert c >= a
    assert a >= b
    assert not b >= c
    
    # __lt__()
    assert a < c
    assert not a < b
    
    # __le__()
    assert b <= a
    assert not c <= b
    
    # __add__()
    assert a + b == (1, 1)
    assert a + c == (5, 4)
    
    # __sub__()
    assert a - b == (0, 1)
    assert a - c == (-1, 4)
    
    # __mul__()
    assert a * b == (1, 4)
    assert a * c == (3, 8)
    
    # __truediv()__
    assert a / c == (2, 3)
    assert c / c == (1, 1)   