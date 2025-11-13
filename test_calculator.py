import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Add the following test methods to the TestCalculator class:
#Add
    #case1
    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    #case2
    def test_add2(self):
        self.assertEqual(self.calc.add(2, 4), 6)

#Subtract
    #case1
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    #case2
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)

#Multiply
    #case1
    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    #case2
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(10, 2), 20)

#Divide
    #case1
    def test_divide1(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
    #case2
    def test_divide2(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

#Modulo
    #case1
    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    #case2
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

if __name__ == '__main__':
    unittest.main()