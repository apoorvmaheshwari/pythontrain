#Anonymous function
#Inline function
#lambda function

'''
Rule1: function should contain only 1 line
Rule2: that 1 line should be return statement

def sayhi(n1,n2):
	return "Hi "+n1+" "+n2
'''
hello =lambda n1,n2: "Hi "+n1+" "+n2
print(type(hello))
print(hello("A","B"))
print(hello("C","D"))
print(hello("E","F"))