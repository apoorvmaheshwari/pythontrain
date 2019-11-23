myvar=lambda x: x**2


print('Output:',myvar(4) + myvar(5))









(lambda x:(float(9)/5)*x + 32)(0)
f = (lambda x,y: x**2 + (lambda z :z**2)(y))

print(f(2,3))


power=lambda x : lambda y: y**x
square = power(2)
cube=power(3)
print(square(3))
print(cube(3))










Celsius = [39.2, 36.5, 37.3, 37.8]
list(map(lambda x: x * 2 + 10, Celsius))