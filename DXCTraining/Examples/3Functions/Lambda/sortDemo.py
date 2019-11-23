def myfilter(x):
	return x>25

foo = [2, 18, 9, 42, 17, 26,55,32]
#mapdata=map(lambda x: x**2, foo)
filterdata=filter(myfilter,foo)
print(list(filterdata))





















'''
data=[{'name':'shirts','cost':1000},{'name':'shoes','cost':3000},{'name':'tie','cost':400}]

data.sort(key=lambda x: x['cost'],reverse=True)

print(data)
'''

