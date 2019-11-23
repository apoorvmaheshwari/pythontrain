for num in range(2,20):  
   for i in range(2,num):
      if num%i == 0: break      	 
   else:                  
      print(num)

a=0
b=1
print a
for i in range(10):
	a,b=b,a+b
	print a