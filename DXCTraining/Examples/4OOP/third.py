class Emp:
	count=0
	def __init__(self,name,dept,id):
		Emp.count+=1
		self.name=name
		self.dept=dept
		self.id=id
	def getDept(self):
		return self.dept
	@staticmethod
	def dispCount(w):
		print(Emp.count)
	@classmethod
	def getCount(rt):
		print(rt)
		return(rt.count)
e1=Emp('Saravan','NSN',53898)
e1.dispCount(Emp('a','b',0))
print(Emp.getCount())

'''
class Stu:
	pass
s1=Stu()
s1.name='Vamsi'
Emp.dispCount(s1)

'''