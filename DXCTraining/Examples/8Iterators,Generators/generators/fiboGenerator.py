
def MyFibo(i):
	a,b,j=0,1,1
	while(j<i):
			yield a 
			a,b=b,a+b	
			j+=1

for x in MyFibo(56):
	print(x)





