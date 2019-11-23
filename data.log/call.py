class person:
    '''
    This is for OOP demo
    '''
    team = "India"

    def sayHi(p):
        print("Hi all" + " " + p.fname + " " + p.lname)

    def __init__(o, f, l):
        o.fname = f
        o.lname = l

obj=person("Sachin","Tendulkar")
print(person.__name__)

print(person.__module__)
print(person.__doc__)
print(person.__dict__)
