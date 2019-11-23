class NameNotInList(Exception):
    def __init__(self, value="Invalid Data encountered,a valid data expected"):
        self.value = value
    def __str__(self):
        return self.value	

class UnderAgeError(Exception):
    def __init__(self, value="User is under age"):
        self.value = value
    def __str__(self):
        return self.value	

def cred():
	while(True):
		try:		
			li= ['Sachin' ,'Bhargava' , 'Saurav' , 'Sehwag' ,'Dhoni']	
			uname= None
			uname= input('Enter Username:')
			if uname not in li:
				raise NameNotInList
			age= input('Enter Age')
			if int(age) <18:
				raise UnderAgeError
			return uname
		except NameNotInList as e:
			print(e)
			continue
		except UnderAgeError as e:
			print('User not allowed!')
			continue
uname=cred()
if(uname):
	print('Welcome',uname)
		





		
		
		
		
		
		
		
		
'''		
try:
	raise StopIteration
except Exception as e:
	print(e)
finally:
	print('this was final')

print('Here I can continue')
'''