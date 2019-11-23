try:
	a=int(input("Enter number"))
	b=int(input("Enter number"))
	division=a/b
	print("data : ",division)
except (ZeroDivisionError,ValueError) as e:
	print("Please enter non zero numeric value!")
except Exception as e:
	print("Generic handler!")
print("Some other important task")
