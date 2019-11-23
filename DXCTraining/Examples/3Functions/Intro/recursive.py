def showNumbers(start,end):
	if(start<end):
		showNumbers(start+1,end)
		print start
		
#showNumbers(0,3)

def recFibo(a,b):
	if(a<13):
		print a
		recFibo(b,a+b)
#recFibo(0,1)

def fact(n):
	if(n==0):
		return 1
	return n*fact(n-1)
print fact(3)