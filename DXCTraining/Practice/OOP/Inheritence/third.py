class person:
	nationality="India"#class level encapsulation
	def sayhi(spiderman):
		print("Hi "+spiderman.fname+" "+spiderman.lname)
	def __init__(superman,fname,lname):
		superman.fname=fname
		superman.lname=lname
class employee(person):
	org="DXC"
	def __init__(superman,fname,lname,dept,loc):
		person.__init__(superman,fname,lname)
		superman.dept=dept
		superman.loc=loc
	def work(obj):
		print(obj.fname+" is working!")
class student(person):
	institute="Python University"
	def __init__(self,fname,lname,stream):
		person.__init__(self,fname,lname)
		self.stream=stream
	def study(self):
		print(self.fname+" is studying!")
e1=student("Sachin",
			"Tendulkar",
			"Sports")
e1.study()
e1.sayhi()
print(e1.__dict__)