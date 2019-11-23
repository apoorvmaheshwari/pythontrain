obj=[
	{
	"fname":"Sachin",
	"lname":"Tendulkar",
	"city":"Bengaluru"
	},
	{
	"fname":"Saurav",
	"lname":"Ganguly",
	"city":"Mumbai"
	},
	{
	"fname":"Rahul",
	"lname":"Dravid",
	"city":"Kolkata"
	}]

obj.sort(key=lambda el:el["fname"])
print(obj)