class student: 
 def __init__(self, name,perc):  self.name=name  self.perc=perc  def __gt__(self,other):    if self.perc>other.perc:      return True       
    else:      return False
s1,s2,s3=student("vamsi",90),student("pasu",91),student("vasu",23)

if(s1>s2):
 if(s1>s3):
  print(s1.name)
 else:
  print(s3.name)
elif(s2>s3):
 print(s2.name)
else:
 print(s3.name)
 