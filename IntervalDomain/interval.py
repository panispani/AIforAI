def relu(I1):
    (from1, to1) = I1
    return (max(from1,  0), max(to1, 0))