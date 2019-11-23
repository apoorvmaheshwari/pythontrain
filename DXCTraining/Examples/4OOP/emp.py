class Emp:
    count=0
    def __init__(self,name,dept):
        if(Emp.count==1):
         print("Only one object can be created")
         del(self)
        else:
         self.name=name
         self.dept=dept
         Emp.count+=1
    def __del__(self):
     print("Destructor was called for Employee id", id(self))    
    
    def  getCount():
        return Emp.count
    def dispEmp(self):
        print("NAME:%s , DEPARTMENT:%s"%(self.name,self.dept))

emp1=Emp("JOHN","Accounts")
emp2=Emp("Smith","Accounts")
print(id(emp1),"  ",id(emp2))
print(type(emp1))
print(type(emp2))

