'''
class A:
	class B:
		count=0
		
obj = A.B()
print(obj.count)
'''
############################################
outer=123
def a():
	def b():
		c= secret+1
		return c
	secret=0
	return b
	
x=a()()
print(x)
