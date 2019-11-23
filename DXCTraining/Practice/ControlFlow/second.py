marks=int(input('Enter marks'))

if marks>=0  and marks<=100:
	if marks<40:
		print("FAIL")
	elif marks<60:
		print("THIRD")
	elif marks<80:
		print("SECOND")
	else:
		print("FIRST")
else:
	print("Invalid")


	   
	   
	   
