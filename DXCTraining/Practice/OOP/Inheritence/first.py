class person:
	nationality="India"#class level encapsulation
	def sayhi(spiderman):
		print("Hi "+spiderman.fname+" "+spiderman.lname)
class employee(person):
	org="DXC"
	def work(obj):
		print(obj.fname+" is working!")
e1=employee()
e1.fname="Sachin"
e1.lname="Tendulkar"
e1.work()
e1.sayhi()
print(e1.org , e1.nationality)