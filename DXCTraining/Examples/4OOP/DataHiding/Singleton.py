class SingletonDemo:
	__count=0
	__obj=None
	def getInstance():
		if(SingletonDemo.__count>0):
			return SingletonDemo.__obj
		else:
			SingletonDemo.__obj=SingletonDemo()
			SingletonDemo.__count+=1
			return SingletonDemo.__obj
obj=SingletonDemo()
obj=SingletonDemo.getInstance()
obj2=SingletonDemo.getInstance()
print(id(obj)==id(obj2))