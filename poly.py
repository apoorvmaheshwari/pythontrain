class person:
    nationality = "Indian"

    def sayhi(self):
        print("Hi" + self.f)

    def __init__(o, f):
        o.f = f

    def __int__(self):
        return len(self.f)

    def __str__(self):
        return '{f}'.format(**self.__dict__)


p1 = person("Sachin")

print(int(p1))
print(str(p1))
print(p1)
