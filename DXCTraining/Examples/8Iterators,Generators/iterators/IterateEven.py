class Myrange:
    def __init__(self,i, n):
        self.n = n
        self.i = i
    def __iter__(self):
        return Myrange_iter(self.i,self.n)

class Myrange_iter:
	def __init__(self, i,n):
		self.i = i
		self.n = n

	def __next__(self):
		while self.i < self.n:
			if(self.i%2==0):
				i = self.i
				self.i += 1
				return i
			else:
				self.i += 1
		else:
			raise StopIteration()

#m1=Myrange(10)
#m2=iter(m1)
'''
print(m2.__next__())
print(m2.__next__())
print(m2.__next__())
print(m2.__next__())
print(m2.__next__())

'''
for x in Myrange(100,120):
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