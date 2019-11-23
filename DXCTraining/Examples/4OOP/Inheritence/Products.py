class Product:
	__count=0
	def __init__(self,name,cost):
		Product.__count+=1
		self.id=Product.__count
		self.name=name
		self.cost=cost
		
class Order:
	__count=0
	def __init__(self,pdict,c):
		Order.__count+=1
		self.id=Order.__count
		self.pdict=pdict
		self.customer=c
	def getBill(self):
		return { k.id:k.cost*v for (k,v) in zip(self.pdict.keys(), self.pdict.values())}
class Customer:
	__count=0
	placedOrders=[]
	def __init__(self ,name , address):
		Customer.__count+=1
		self.id=Customer.__count
		self.name=name
		self.address=address
	def placeOrder(self,pdict):
		OrderObj= Order(pdict,self)
		self.placedOrders.append(OrderObj)
		return OrderObj
		

pObj1=Product('shirts',3000)
pObj2=Product('shoes',5000)
pObj3=Product('goggs',1200)
pObj4=Product('sandals',6000)
customer1=Customer('Bhargava' , 'JP Nagar')
customer2=Customer('Saravan' , 'OTP')
customer3=Customer('Hari Priya' , 'Madiwala')
order= customer1.placeOrder({pObj1:4,pObj3:1})
print(sum(order.getBill().values()))