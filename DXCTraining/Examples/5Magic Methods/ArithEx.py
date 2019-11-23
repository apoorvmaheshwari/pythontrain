class Arithmetic:
 n=0
 def __init__(self,n=0):
  self.n=n
 def __add__(self,other):
  r=Arithmetic()
  r.n= self.n+other.n
  return(r)
 def __str__(self):
  s="Object of class Arithmetic value="+str(self.n)
  return s
a1,a2 =Arithmetic(10),Arithmetic(20)
r=a1+a2
print(a1,a2,r)

"""
Student
name-instance variables
perc-instance variables

s1 s2 s3

print names of students rankwise in class

..................
print names of students in alphabetical order
"""