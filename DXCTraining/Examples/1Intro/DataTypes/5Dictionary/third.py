dict1={'fname1':'Sachin','lname1':'Tendulkar'}
dict2={'fname2':'Rahul','lname2':'Dravid'}
dict1.update(dict2)
#print(dict1)



D1 = { k:v for (k,v) in zip(dict1.keys(), dict1.values())}
print(D1)


