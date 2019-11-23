
#list of list of 10's complement 
li=[ [x,y,z] for x in range(1,10) for y in range(x,10) for z in range(y,10)if x+y+z==10 ]
print(li)

n=int(input('Enter no.: '))
li=[x for x in range(1,n+1) if n%x==0 ]
	