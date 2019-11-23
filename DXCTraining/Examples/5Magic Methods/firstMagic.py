class B:
 pass
class A:
 attrs={}
 def __init__(self):
  print('constructor!')
 def __new__(cls):
   l=[1,2,3,4]
   
 def __setattr__(self,attr,val):
  self.attrs[attr]=val
 def __getattr__(self,attr):
  return(self.attrs[attr])


