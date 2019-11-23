
def decor(someFunction):
	def inner(*args,**kwargs):
			print('function called')
			someFunction(*args)
			print('function finished execution')
	return inner

@decor
def getData(a,c):
 print("this getData stmt: "+str(a)+str(c))

getData(1,2)
