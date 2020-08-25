
import sys; from os.path import dirname, abspath; sys.path.append(dirname(dirname(abspath(__file__))))
from calculator import Calculator

def test_add():

	n1, n2 = 4, 20

	calc = Calculator(n1, n2)

	assert calc.add() == n1 + n2, "The method 'add' returned a different value!"


def test_sub():

	n1, n2 = 4, 20

	calc = Calculator(n1, n2)

	assert calc.subtract() == n1 - n2, "The method 'subtract' returned a different value!"