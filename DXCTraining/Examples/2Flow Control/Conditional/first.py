a,b,c=int(input('Enter a number')),int(input('Enter another number')),int(input('Enter another number'))
if(a>b):
	if a>c:
		print(a,'is greater')
	else:
		print(c,'is greater')
else:
	if b>c:
		print(b,'is greater')
	else:
		print(c,'is greater')