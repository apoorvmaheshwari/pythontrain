'''def myfirst(name):
	print 'Hi %s this is a function call'%name
myfirst('Sachin')'''

def isEven(n):
	return n%2==0
	

	
def isPrime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	else:
		return True			


	
#val = isPrime(6)
#print val

def nthFibo(n):
	a,b=0,1
	
	for i in range(2,n+1):
		a,b=b,a+b
	return a

print nthFibo(4)







