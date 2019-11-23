#list comprehensions
 
list0=[x*2 for x in range(10)]






list2=[(x,y,z) for x in range(11) for y in range(x,11) for z in range(y,11) if x+y+z==10]











l1 = [(x,x**2) for x in range(10)]


l2 = [2**i for i in range(13)]




















l3 = [x for x in list0 if x % 2 == 0]
 
l4 = [(x,x**2) for x in range(10)]
 
 
 
 nonprimes=[x for x in range(2,100) for y in range(2,x) if(x%y==0 ) ]
 
 
 
 
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ (x,(float(9)/5)*x + 32) for x in Celsius ]


print Fahrenheit




 {j:[x for x in range(1,j+1) if j%x==0] for j in range(2,50)  }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#Pythagorean triplets
print [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]

 
#primes and no primes (sieve of Eratosthenes)
notprimes = list(set([j for i in range(2, 8) for j in range(i*2, 50, i)]))
primes = [x for x in range(2, 50) if x not in notprimes]
print primes
 