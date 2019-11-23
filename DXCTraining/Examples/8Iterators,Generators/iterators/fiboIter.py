
class Myrange:
	def __init__(self, limit):
		self.limit = limit

	def __iter__(self):
		m=Myrange_iter(self.limit)
		return m

class Myrange_iter:
	def __init__(self, limit):
		self.a = 0
		self.b= 1
		self.count = 1
		self.limit = limit
	def __next__(self):
		if self.count < self.limit:
			self.a,self.b=self.b,self.a+self.b
			self.count+=1
			return self.a
		else:
			raise StopIteration()
m=Myrange(10)		
for i in m:
	print(i)
	for i in m:
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