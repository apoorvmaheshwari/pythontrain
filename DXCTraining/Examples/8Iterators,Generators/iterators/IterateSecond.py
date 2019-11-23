class Myrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Myrange_iter(self.n)

class Myrange_iter:
	def __init__(self, n):
		self.i = 0
		self.n = n
	def __next__(self):
		while(self.i < self.n):
			i = self.i
			self.i += 1
			if i%7==0 :
				return i
			else:
				continue
		else:
			raise StopIteration()

m1=Myrange(100)
for x in m1:
	print(x)







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