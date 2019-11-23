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
		self.start = 2
		self.limit = limit
	def __next__(self):
		if self.start < self.limit:
			while(True):
				if(isPrime(self.start)):
					break
				else:
					self.start += 1
			old=self.start
			self.start += 1
			return old
		else:
			raise StopIteration()

m1=Myrange(25)
m2=iter(m1)

for i in Myrange(100):
	print(i)














"""
for x in Myrange(10):
 print(x)
"""

"""
Myrange is Iterable ,Myrange_iter is the Iterator ,Iterators are Iterable

Reverse iterate a list.
create a sort_iter for a list.
Iterate a list of names in alphabetical order

"""