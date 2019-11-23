obj=[22,32,19,43]

newobj=map(lambda el:32+el*9/5,obj)
print(type(newobj))
for i in newobj:
	print(i)