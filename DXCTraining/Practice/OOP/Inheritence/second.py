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
class manager(employee):
	def __init__(self,fname,lname,dept,loc,reportees):
		employee.__init__(self,fname,lname,dept,loc)
		self.reportees=reportees
	def manage(self):
		print(self.fname+" is managing!")
e1=manager("Sachin",
			"Tendulkar",
			"Batting",
			"Mumbai",
			[])
e1.work()
e1.sayhi()
e1.manage()
print(e1.__dict__)