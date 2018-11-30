
def relu(I1):
    """Calculate the relu of an interval as another interval

    Keyword arguments:
    I1 -- the interval given as a tuple (a, b)
    """
    (from1, to1) = I1
    return (max(from1,  0), max(to1, 0))

def relu_number(n):
    """Calculate the relu of a number

    Keyword arguments:
    n -- the number
    """
    return max(0, n)

def add(I1, I2):
    """Calculate the addition of two intervals as another interval

    Keyword arguments:
    I1 -- the first interval given as a tuple (a, b)
    I2 -- the second interval given as a tuple (c, d)
    """
    (from1, to1) = I1
    (from2, to2) = I2
    return (from1 + from2,  to1 + to2)

def sub(I1, I2):
    """Calculate the substraction of two intervals as another interval

    Keyword arguments:
    I1 -- the first interval given as a tuple (a, b)
    I2 -- the second interval given as a tuple (c, d)
    """
    (from1, to1) = I1
    (from2, to2) = I2
    return (from1 - max(from2, to2),  to1 - min(from2, to2))

def mul_constant(I1, n):
    """Calculate the multiplication of an interval by a constant

    Keyword arguments:
    I1 -- the interval given as a tuple (a, b)
    n -- the real constant to multiply with
    """
    (from1, to1) = I1
    return (min(from1 * n, to1 * n), max(from1 * n, to1 * n))

def to_interval(num):
    """Convert the input number to a thin interval

    Keyword arguments:
    n -- the number to convert to an interval
    """
    return (num, num)
