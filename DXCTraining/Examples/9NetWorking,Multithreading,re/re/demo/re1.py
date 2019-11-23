import re
data=input('Enter data :')
if re.search('^[a-zA-Z0-9]*$',data):
	print('Allowed!!')
else:
	print('FAIL!')
