def allstrings(a):
	def inner(*args,**kwargs):
		for i in args:
			if type(i)!=str:
				print("Invalid args")
				break
		else:
			for i  in kwargs.values():
				if type(i)!=str:
					print("Invalid args")
					break
			else:
				a(*args,**kwargs)
		
		
	return inner
@allstrings	
def hello(name):
	print("hello "+name)
@allstrings	
def sayhi(name1,name2):
	print("hi "+name1+" "+name2)
hello("Sachin")
sayhi(name2="Sachin",name1="Rahul")
hello(1)
sayhi(True)