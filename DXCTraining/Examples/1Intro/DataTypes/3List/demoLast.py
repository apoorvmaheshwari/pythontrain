li=[
	{'id':1 ,'name': 'shoes','cost':5000,'brand':'reebok' },
	{'id':2 ,'name': 'shoes','cost':6000,'brand':'adidas' },
	{'id':3 ,'name': 'shoes','cost':4000,'brand':'nike' },
	{'id':4 ,'name': 'shoes','cost':3000,'brand':'lotto' },
	{'id':5 ,'name': 'shirts','cost':2000,'brand':'lotto' },
	{'id':6 ,'name': 'shirts','cost':1700,'brand':'arrow' },
	{'id':7 ,'name': 'shirts','cost':2000,'brand':'adidas' },
	
   ]

choice=int(input('''Enter choice
					(1 by name ,
					2 by brand,
					3 by cost L 2 H
					4 by cost H 2 L): '''))

sli=[
	lambda x:x['name'],
	lambda x:x['brand'],
	lambda x:x['cost'],
	lambda x:x['cost']
	]
rli=[
	False , 
	False , 
	False,
	True
	]
li.sort(key=sli[choice-1] , reverse=rli[choice-1])

#print(li)
t='id:{id} , name:{name},cost:{cost} , brand:{brand}'
for el in li:
	print(t.format(**el))
	