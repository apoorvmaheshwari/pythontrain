class person:
    team = "India"
    def sayhi():
        print("Hi All")


obj = person()
print(type(obj))
obj.fname = "Sachin"
obj.lname = "Tendulkar"

print(obj.fname, obj.lname, obj.team, obj.__class__.team)


obj2 = person()
print(type(obj))
obj2.fname = "Rahul"
obj2.lname = "Dravid"
obj2.team = "Australia"
print(obj2.fname, obj2.lname, obj2.team, obj2.__class__.team)
print(person.team)
person.sayhi()