Celsius = [39.2, 36.5, 37.3, 37.8,10.0,12.0,23.0]

def myFilter(myFun,li):
	myList=[]
	for data in li:
		if myFun(data):
			myList.append(data)
	return myList

def myreduce(myFun,li):
	iterVal=li[0]
	c=1
	while c< len(li):
		iterVal=myFun(iterVal,li[c])
		c+=1
	return iterVal


print(myreduce(lambda x, y: x * y+30, Celsius))



'''
ccl=myFilter(lambda x: x<25, Celsius)	
print(ccl)
'''