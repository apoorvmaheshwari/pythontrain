class Std:
	name=''
	marks=''
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks

	def __lt__(self,other):
		return self.marks<other.marks
	
li=[Std('Saravan',100),Std('Bhargava',20),Std('Shashank',0)]
li.sort(key=(lambda x: x.marks))
for s in li :
	print(s.name)