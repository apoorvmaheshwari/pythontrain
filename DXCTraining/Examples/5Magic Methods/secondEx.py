class B
pass







class A:
 attrs={}
 def __init__(self):
  pass
 def __setattr__(self,attr,val):
  self.attrs[attr]=val
 def __getattr__(self,attr):
  return(self.attrs[attr])
 
b=B()
b.i=10
print(b.i)
a=A()
a.i=10
print(a.i)
