class T:
 def test(self):
  print("Thiswas a test")


class A(T):
    def __init__(self):
        super().__init__()
        print('B.__init__')
class B(T):
    def __init__(self):
        super().__init__()
        print('A.__init__')
        

        
class C(B,A):
    def __init__(self):
        super().__init__()
        print('C.__init__')
        
c= C()


"""
class Product:
 __init__(self,id,cost)

class Order
 def __init__(self,prod,quantity)
  ....



  Order o1,o2
  o2+o1  