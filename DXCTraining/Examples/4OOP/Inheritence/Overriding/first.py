class Person:
	nationality='Indian'
	def __init__(self):
		self.name='Saravan'
	def sayHi(self):
		print('Hi')
		
class Emp(Person):
		def __init__(self):
			super().__init__()
			self.dept='SNS'
			self.id='007'

e1 = Emp()
print(e1.name)
print(e1.__dict__)
print(Emp.__bases__)
