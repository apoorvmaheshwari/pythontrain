li1=[1,2,3]
li2=['a','b','c']
'''
D3 = dict(zip(li1, li2))
print(D3)
D4 = dict(zip(li2, li1))
print(D4)

print(type(zip(li1, li2)))
'''



D1 = { k:v for (k,v) in zip(li1, li2)}
print(D1)

