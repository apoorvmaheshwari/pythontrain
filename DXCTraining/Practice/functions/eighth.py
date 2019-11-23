def outer():
	count=0
	def inner():
		nonlocal count
		count+=1
		print(count)
	return inner
		
hello=outer()
hello()
hello()
hi=outer()
hello()
hello()
hello()
hi()
hi()
hi()
hi()
	