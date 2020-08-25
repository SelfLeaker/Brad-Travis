
class Calculator(object):

	def __init__(self, n1, n2):

		self.n1 = n1
		self.n2 = n2

	def add(self):

		return self.n1 + self.n2 + 1

	def subtract(self):

		return self.n1 - self.n2

if __name__ == "__main__":

	calc = Calculator(4, 20)

	print(calc.add(), end="")