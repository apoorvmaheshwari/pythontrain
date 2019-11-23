def y():
	pass

class A:
	sam='test'
class Person:
	count=0
	def __init__(self,name):
		Person.count+=1
		self.name=name
	def sayHi(self):
		print('Hi '+self.name)
class Emp(Person,A):
	def __init__(self,name,id):
		super().__init__(name)
		self.id=id
	def sayHi(self):
		super().sayHi()
		print('Hello  '+self.name)
		
e1 = Emp('Saravan' ,'007')
e1.sayHi()







#e1.sayHi()
#print(e1.__dict__)
#print(Emp.__dict__)
#print(Person.__dict__)
#print(Emp.__bases__)



#z=type('Foo', (), {'attrib': 'value'}) #meta class
		