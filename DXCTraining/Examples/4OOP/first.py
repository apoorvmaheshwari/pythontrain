class Emp:
	count=0
	def __init__(self,name,dept,id):
		Emp.count+=1
		self.name=name
		self.dept=dept
		self.id=id
	def getDept(self):
		return self.dept
	def dispCount():
		print(Emp.count)
e1=Emp('Saravan','NSN',53898)
#e2=Emp('Bhargava','NSN',54024)
print(e1)
