li=[{'id':1,'cost':12000},{'id':2,'cost':1200},{'id':3,'cost':2000},{'id':4,'cost':20}]

def liComparator(o):
	return o['cost']

li.sort(key=liComparator)
