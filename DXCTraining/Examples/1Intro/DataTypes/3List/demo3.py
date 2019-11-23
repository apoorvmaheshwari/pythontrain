# one liner function ,that one line should be return statement.




outer = lambda y: lambda x:x**y
square=outer(2)
cube=outer(3)
print(square(3))
print(square(4))
print(square(5))
print(cube(3))
print(cube(4))
print(cube(5))
