
celcius=[{'name': 'Ahemdabad' ,'temp':32},
{'name': 'Jodhpur' ,'temp':45},{'name': 'Pune' ,'temp':25},
{'name': 'Hyderabad' ,'temp':33},{'name': 'Coorg' ,'temp':22}]


def mymap(d): 
		return d['temp']*9/5+32
		
		

fahrenheit=map( mymap,celcius)

print(list(fahrenheit))
