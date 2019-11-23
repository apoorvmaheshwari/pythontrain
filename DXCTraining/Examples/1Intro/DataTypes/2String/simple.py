temp="Hello {0} {1} ,welcome to {2}"
data=temp.format("Sachin","Tendulkar","Bangalore")
print(data)

temp="Hello {fname} {lname} ,welcome to {city}"
data=temp.format(fname="Sachin",
				lname="Tendulkar",
				city="Bangalore")
print(data)

d= {"fname":"Sachin",
	"lname":"Tendulkar",
	"city":"Bangalore"}
print(temp.format(**d))