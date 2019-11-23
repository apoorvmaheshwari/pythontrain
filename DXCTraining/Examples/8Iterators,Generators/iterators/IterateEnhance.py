def isPrime(n):
	i=2
		while(i<n):
		if(n%i==0):
			return False
		i+=1
	else:
		return True
class Myrange:
	def __init__(self, limit):
		self.limit = limit
	def __iter__(self):
		m=Myrange_iter(self.limit)
		return m

class Myrange_iter:
	def __init__(self, limit):
		self.start = 0
		self.limit = limit
	def __next__(self):
		if self.start < self.limit:
			self.start += 1
			return self.start*2
		else:
			raise StopIteration()

m1=Myrange(4)
m2=iter(m1) # m1.___iter__()
'''
print(m2.__next__())
print(m2.__next__())
print(m2.__next__())
print(m2.__next__())
print(m2.__next__())
'''
for m in m1:
	print(m)


for x in Myrange(10):
	print(x)










"""
Reverse iterate a list.
create a sort_iter for a list.
Iterate a list of names in alphabetical order

"""