class A:
	def __init__(self,a):
		self.a=a
	def sayHi(self):
		print('Hi of A')
class B:
	def __init__(self,b):
		self.b=b
	def sayHi(self):
		print('Hi of B')
class C(A,B):
	def __init__(self,a,b,c):
		A.__init__(self,a)
		B.__init__(self,b)
		self.c=c
	def sayHi(self):
		print('Hi of C')
cObj = C(12,2,3)
A.sayHi(cObj)
B.sayHi(cObj)
cObj.sayHi()
print(cObj.__dict__)
	