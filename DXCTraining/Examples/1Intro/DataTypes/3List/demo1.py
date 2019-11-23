li=[
	{'name':'Bangalore', 'temp':24 },
	{'name':'Mumbai' ,'temp':30 },
	{'name':'Chennai' ,'temp':32 },
	{'name':'Delhi','temp':35 },
	{'name':'Pune','temp':24},
	{'name':'Ooty','temp':22 },
	{'name':'Ladakh','temp':18 }
   ]
def myfilter(el):
	return el['temp']<25
	
data= filter(myfilter,li)
print(type(data))
for d in data:
	print(d)