astring='Hello Wooooorld!'
i=0
k= 0
while i<astring.count('o'):
	k= astring.index('o',k+1)
	i+=1
print(k)