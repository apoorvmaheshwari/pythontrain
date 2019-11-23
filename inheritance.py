class person:
    nationality = "India"

    def sayHi(self):
        print("Hi " + self.fname + " " + self.lname)

    def __init__(x, fname, lname):
        x.fname = fname
        x.lname = lname


class employee(person):  # employee inherits person class
    org = "DXC"

    def __init__(x, fname, lname, dept, location):  # constructor chaining
        # super().__init__(fname,lname) #works,but dont use super

        person.__init__(x, fname, lname)
        x.dept = dept
        x.location = location

    def work(obj):
        print(obj.fname + " is working")


class manager(employee):  # employee inherits person class

    def __init__(x, fname, lname, dept, location, reportees):  # constructor chaining
        # super().__init__(fname,lname) #works,but dont use super

        employee.__init__(x, fname, lname, dept, location)

        x.reportees = reportees

    def manage(self):
        print(self.fname + " is managing")


class student(person):
    institute: "Python Uni"

    def __init__(self, fname, lname, stream):
        person.__init__(self, fname, lname)
        self.stream = stream

    def study(self):
        print(self.fname + " is studying")


class intern(student, employee):
    def __init__(self, fname, lname, dept, location, stream):
        student.__init__(self, fname, lname, stream)
        employee.__init__(self, fname, lname, dept, location)


# e1=employee("Sachin","Tendulkar")
# e1.fname="Sachin"
# e1.lname="Tendulkar"
e1 = manager("Sachin", "Tendulkar", "DTC", "Bangalore", [])
e2 = student("Sachin", "Tendulkar", "Sports")  # constructor overriding
e3 = intern("Sachin", "Tendulkar", "Batting", "Mumbai", "Sports")
e1.work()
e1.sayHi()
e1.manage()
e2.study()
e2.sayHi()

e3.study()
e3.sayHi()
e3.work()
print(e1.org, e1.nationality)
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)

print(employee.__bases__)
print(student.__bases__)
print(manager.__bases__)
print(person.__bases__)
print(intern.__bases__)
