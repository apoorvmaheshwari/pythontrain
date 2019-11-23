class Base:
    def __init__(self):
        print('Base.__init__')
    def simpleMethod(self):
        print("Base Method")        

class Child(Base):
    def __init__(self):
        
        print('C.__init__')
    def simpleMethod(self):
        super().simpleMethod()
        print("Child Method")


    
        
c= Child()
c.simpleMethod()


