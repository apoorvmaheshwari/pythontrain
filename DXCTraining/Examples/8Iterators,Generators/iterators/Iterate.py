class Myrange:
 def __init__(self, start,lim):
  self.start = start
  self.lim = lim
 def __iter__(self):
  return self
 def __next__(self):
  if self.start < self.lim:
   i = self.start
   self.start += 1
   return i
  else:
   raise StopIteration()


a1=Myrange(10,20)
a1.__next__()
a1.__next__()
a1.__next__()
a1.__next__()
print('Loop Starts:')
for x in a1:
 print(x)


"""
OddRange , PrimeRange , FiboRange , ReverseRange
"""