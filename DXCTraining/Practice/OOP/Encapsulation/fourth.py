
class person:
	'''
	this idemo for oop concpets
	'''
	team="India"#class level encapsulation
	def sayhi(spiderman):
		print("Hi "+spiderman.fname+" "+spiderman.lname)
	def __init__(o,f,l):
		o.fname=f
		o.lname=l
obj=person("Sachin","Tendulkar")
print(obj.__name__)
print(obj.__module__)
print(obj.__doc__)
print(obj.__dict__)
# print(person.__bases__)





