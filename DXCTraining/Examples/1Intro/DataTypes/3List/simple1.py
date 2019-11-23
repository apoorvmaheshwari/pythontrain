obj=[
	{"team":"India","fname":"Sachin","lname":"Tendulkar"},
	{"team":"India","fname":"Saurav","lname":"Ganguly"},
	{"team":"India","fname":"Rahul","lname":"Dravid"},
	{"team":"Australia","fname":"Steve","lname":"Waugh"},
	{"team":"Australia","fname":"Brett","lname":"Lee"},
	{"team":"Australia","fname":"Ricky","lname":"Ponting"}
	
	]
def myfilter(el):
		return el["team"]=="India"
newobj=filter(myfilter,obj)
print(type(newobj))
for i in newobj:
	print('{fname} {lname}'.format(**i))