def MyListDisp(li ,i):
		while(i<=len(li)):
			yield li[-i] 
			i+=1

li=[1,2,34,5,6]

d=MyListDisp(li,1)
for x in d:
	print(x)
d=MyListDisp(li,1)
for x in d:
	print(x)	


#lidata=[x for x in MyListDisp(li,0)]