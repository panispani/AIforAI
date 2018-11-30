from interval import *
import numpy as np
import unittest

def NNconcrete(x1, x2):
    """Concrete neural network of 2 inputs that we want to abstract

    Keyword arguments:
    x1 -- first input
    x2 -- second input
    """
    return relu_number(relu_number(-x1 + x2 + 2) + relu_number(x1 - 2 * x2))

def NNabstract(x1, x2):
    """Abstracted neural network that takes 2 numbers as inputs
    and outputs an interval that captures the concrete output

    Keyword arguments:
    x1 -- first input
    x2 -- second input
    """
    I1 = to_interval(x1)
    I2 = to_interval(x2)
    return NNabstractInterval(I1, I2)

def NNabstractInterval(I1, I2):
    """Abstracted neural network that takes 2 Intervals as inputs and outputs
    an interval that captures all the concrete outputs of the input intervals

    Keyword arguments:
    I1 -- the first interval
    I2 -- the second interval
    """
    first_neuron = relu(sub(add(I2, to_interval(2)), I1))
    second_neuron = relu(sub(I1, mul_constant(I2, 2)))
    return relu(add(first_neuron, second_neuron))


class TestInterval(unittest.TestCase):

    def test_NN_abstract(self):
        print("\nTesting exactness of interval abstraction on linear operations")
        tests = [(-3,  2), (2, 5), (-6, -2), (0, 0), (-2, 0), (0, -5)]
        for (x1, x2) in tests:
            self.assertEqual(to_interval(NNconcrete(x1, x2)), NNabstract(x1, x2))
        print("PASSED")

    def findMinimumValue(self):
        mini = 2
        x1 = 0
        x2 = 0
        for f1 in np.linspace(0, 2, 100):
            for f2 in np.linspace(0, 1, 100):
                res = NNconcrete(f1, f2)
                if res < mini:
                    mini = res
                    x1 = f1
                    x2 = f2
        return (x1, x2, mini)

    def findMaximumValue(self):
        maxi = 2
        x1 = 0
        x2 = 0
        for f1 in np.linspace(0, 2, 100):
            for f2 in np.linspace(0, 1, 100):
                res = NNconcrete(f1, f2)
                if res > maxi:
                    maxi = res
                    x1 = f1
                    x2 = f2
        return (x1, x2, maxi)


    def test_NN_abstract_intervals(self):
        print("\nTesting the interval abstraction applied on interval inputs")
        (from1, to1) = (0, 2)
        (from2, to2) = (0, 1)
        (_, _, approx_from) = self.findMinimumValue()
        (_, _, approx_to) = self.findMaximumValue()
        print("Numerical approximation of minimum and maximum: ({}, {})".format(approx_from, approx_to))
        print("The interval is smaller than this but the abstraction is even more inaccurate: {}".format(NNabstractInterval((from1, to1), (from2, to2))))
        print("This abtraction is efficient but not very precise in contrast at both criteria with the zonotope domain")
        print("PASSED")

if __name__ == '__main__':
    unittest.main()
