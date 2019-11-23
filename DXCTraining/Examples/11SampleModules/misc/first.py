class A:
    pass

def firstMethod():
    try:
        raise Exception("I know python!")
    except:
        print "Exception"
        return("sample")


a=A()
if type(a) is A:
    print("not type is true")
else:
    print("NO")


if isinstance(a, A):
    print("instance is true")
else:
    print("NO")
