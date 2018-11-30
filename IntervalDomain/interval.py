def relu(I1):
    (from1, to1) = I1
    return (max(from1,  0), max(to1, 0))

def relu_number(n):
    return max(0, n)

def add(I1, I2):
    (from1, to1) = I1
    (from2, to2) = I2
    return (from1 + from2,  to1 + to2)

def sub(I1, I2):
    (from1, to1) = I1
    (from2, to2) = I2
    return (from1 - max(from2, to2),  to1 - min(from2, to2))

def mul_constant(I1, n):
    (from1, to1) = I1
    return (min(from1 * n, to1 * n), max(from1 * n, to1 * n))
