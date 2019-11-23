def demo():
	print("Hello World!")
	
	
# test=demo()#return of demo is passed
test=demo#reference of demo is passed
print(type(test))
test()