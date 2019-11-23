li=[
	{'fname':'Sachin' ,'lname': 'Tendulkar','team':'India' },
	{'fname':'Ricky' , 'lname':'Ponting','team':'Australia' },
	{'fname':'Rahul' , 'lname':'Dravid','team':'India' },
	{'fname':'Brian' , 'lname':'Lara','team':'West Indies' }
   ]

   
ch= int(input("""
			Enter 1 for fname ,
			Enter 2 for fname reverse,
			Enter 3 for lname"""))

fields=["fname","fname","lname"]
revrs=[False,True,False]
			
li.sort(reverse=revrs[ch-1],key=lambda el:el[fields[ch-1]])
   
   
t='fname:{fname} , lname:{lname},team:{team}'
for el in li:
	print(t.format(**el))