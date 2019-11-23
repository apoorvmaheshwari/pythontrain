def isPrime(n):
	i=2
	while(i<n):
		if(n%i==0):
			return False
		i+=1
	else:
		return True
def MyListDisp(li ,i):
		while(i<len(li)):
			if(isPrime(li[i] )):
				yield li[i] 
			i+=1

li=[1,2,34,5,6]
for x in MyListDisp(li,0):
	print(x)





