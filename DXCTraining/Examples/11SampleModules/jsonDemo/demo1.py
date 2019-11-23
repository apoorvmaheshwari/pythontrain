import json

fo = open('demo.txt', 'r')
data = '''
[
	{
		"id":1,
		"fname":"Sachin" ,
		"lname":"Tendulkar",
		"address":{
					"houseno":17,
					"streetno":19,
					"area":"worli",
					"city":"Mumbai",
					"pin":1223445
					}
	},
	{
		"id":2,
		"fname":"Saurav" , 
		"lname":"Ganguly",
		"address":{
					"houseno":17,
					"streetno":19,
					"area":"worli",
					"city":"Kolkata",
					"pin":1223445
					}
	},
	{
		"id":3,
		"fname":"Rahul" ,
		"lname":"Dravid",
		"address":{
					"houseno":17,
					"streetno":19,
					"area":"Indira nagar",
					"city":"Bangalore",
					"pin":560001
					}
	}
]
'''
li = json.loads(data)
for d in li:
    print(d)
print(li[1]['address']['city'])
fo.close()
