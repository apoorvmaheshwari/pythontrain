class A:

    def sayhi(self):
        print("Say Hi from A")


class B(A):
    def sayhi(self):
        print("Say Hi from B")


class C(B,A):
    pass


e1 = C();
e1.sayhi()
