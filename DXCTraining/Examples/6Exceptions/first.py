class NamenotFound(Exception):
	def __init__(self,msg="Name not in List"):
		super().__init__(msg)
try:
	names=["Sachin","Saurav","Rahul"]
	name=input("Enter name")
	if name not in names:
		raise NamenotFound
	else:
		print("Welcome!!")

finally:
	print("this is finally , it always executes!")
	
	
print("This is some ther independant task")