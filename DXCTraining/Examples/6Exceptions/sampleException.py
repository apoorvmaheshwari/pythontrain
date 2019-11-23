class NameNotInList(Exception):
    def __init__(self, value="Invalid Data encountered,a valid data expected"):
        self.value = value
    def __str__(self):
        return self.value	


print('Enter User name: ')
uname= input()
try:		
	li= ['Sachin' ,'Bhargava' , 'Saurav' , 'Sehwag' ,'Dhoni']	
	if uname not in li:
		raise NameNotInList
	print('Welcome',uname)
except NameNotInList as e:
	print(e)


input()



		
		
		
		
		
		
		
		
'''		
try:
	raise StopIteration
except Exception as e:
	print(e)
finally:
	print('this was final')

print('Here I can continue')
'''