outer = lambda x: lambda z :z**x
square=outer(2)
print(square(3))
cube=outer(3)
print(cube(3))
sqroot=outer(1/2)
print(sqroot(16))