celcius=[{'name': 'Ahemdabad' ,'temp':32},
{'name': 'Jodhpur' ,'temp':45},{'name': 'Pune' ,'temp':25},
{'name': 'Hyderabad' ,'temp':33},{'name': 'Coorg' ,'temp':22}]
coolCities=filter( lambda d:d['temp']<30,celcius)
print(list(coolCities))
