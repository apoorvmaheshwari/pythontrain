def abc(name):
	print('Hi '+name)
	
def caller(func):
	func.__call__('Sachin')
	
caller.__call__(abc)