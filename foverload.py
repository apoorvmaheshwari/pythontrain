class Box:
    def __init__(self, itemList):
        self.itemList = itemList

    def __str__(self):
        return str(self.itemList)

    def __add__(self, other):
        newitems = self.itemList + other.itemList
        b = Box(newitems)
        return b

    def __lt__(self, other):
        return len(self.itemList) < len(other.itemList)


b1 = Box(["item1", "item2"])
b2 = Box(["item3", "item4", "item5"])
b4 = Box(["item6"])
b3 = b1 + b2 + b4
print(b1)
print(b2)
print(b3)
print(b1 > b2)
