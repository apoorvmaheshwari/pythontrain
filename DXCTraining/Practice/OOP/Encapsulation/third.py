
class person:
	team="India"#class level encapsulation
	def sayhi(spiderman):
		print("Hi "+spiderman.fname+" "+spiderman.lname)
	def __init__(o,f,l):
		o.fname=f
		o.lname=l
	def __del__(self):
		print("Destructor called for "+
						self.fname+" "+self.lname)
obj=person("Sachin","Tendulkar")
obj2=person("Rahul","Dravid")
obj.sayhi()
obj2.sayhi()
del obj
del obj2




