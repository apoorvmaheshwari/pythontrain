class person:
    team = "India"

    def sayHi(p):
        print("Hi all" + " " + p.fname + " " + p.lname)

    def __init__(o, f, l):
        o.fname = f
        o.lname = l

    def __del__(self):
        print("Destructor called for" + self.fname)


obj = person("Sachin", "Tendulkar")
obj2 = person("Rahul", "Dravid")
# obj.sayHi()
# obj2.sayHi()
setattr(obj, "pan", "ASDFG")
print(obj.pan)
print(getattr(obj, "pan"))
print(hasattr(obj, "pan"))
delattr(obj, "pan")
print(hasattr(obj, "pan"))
