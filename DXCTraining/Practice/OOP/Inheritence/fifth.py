class person:
	nationality="India"#class level encapsulation
	def sayhi(spiderman):
		print("Hi "+spiderman.fname+" "+spiderman.lname)
	def __init__(o,fname,lname):
		o.fname=fname
		o.lname=lname
	def __int__(self):
		return len(self.fname)+len(self.lname)
	def __str__(self):
		return '{fname} {lname}'.format(**self.__dict__)
	def __bool__(self):
		return bool(self.fname) and bool(self.lname)
p1=person("Sachin","Tendulkar")

print(int(p1))
print(str(p1))
print(p1)
p2=person("","")
print(bool(p2))
	
	