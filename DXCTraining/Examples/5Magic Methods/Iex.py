class A:
 num=0
 def __init__(self,num=0):
  self.num=num
 def __add__(self,other):
  print("self is %d other is %d"%(self.num , other.num))
  n=A()
  n.num = self.num + other.num
  return n
a1=A(1)
a2=A(9)
a3=a1+a2+ A(5)
print(a3.num)
