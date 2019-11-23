class person:
	team="India"#class level encapsulation
	def sayhi(self):
		print("Hi "+self.fname+" "+self.lname)
obj=person()
obj.fname="Sachin"#object level encapsulation
obj.lname="Tendulkar"#object level encapsulation

obj2=person()
obj2.fname="Rahul"#object level encapsulation
obj2.lname="Dravid"#object level encapsulation

person.sayhi(obj2)
obj.sayhi()#translated to person.sayhi(obj)
obj2.sayhi()



