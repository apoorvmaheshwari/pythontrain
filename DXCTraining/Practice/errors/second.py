class NameNotFound(Exception):
	def __init__(self,msg="name not found!"):
		Exception.__init__(self,msg)
try:
	names=["Sachin","Saurav","Rahul"]
	name=input("Enter name: ")
	if name not in names:
		raise NameNotFound
	print("Welcome "+name)
except NameNotFound as e:
	print(e)
except Exception as e:
	print("Generic handler!",e)
print("Some other important task")
