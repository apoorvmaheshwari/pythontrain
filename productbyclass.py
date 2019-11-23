class Products:
    def sayproducts(self):
        print("The details of products are")
        print("id" + "" + str(self.id) + "name" + " " + self.name + "cost: " + str(self.cost))

    def __init__(o, i, n, c, b, r, d, ca):
        o.id = i
        o.name = n
        o.cost = c
        o.brand = b
        o.rating = r
        o.discount = d
        o.category = ca


choice = int(input("Enter index"))
li2 = ["id", "name", "cost", "brand", "rating", "discount", "category"]
li = [Products(1, "Mango", 10, "Alphanso", 4, 10, "Fruits"), Products(2, "Apple", 50, "Himachal", 4, 20, "Fruits"),
      Products(3, "Banana", 2, "yayaya", 4, 10, "Fruits")]
print(li)

li.sort(key=lambda el: getattr(el, li2[choice]))
for i in li:
    i.sayproducts()
