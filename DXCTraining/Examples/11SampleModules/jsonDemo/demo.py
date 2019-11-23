import json

fo = open('demo.txt', 'r')
li = json.load(fo)
for d in li:
    print(d)
print(li[1]['address']['city'])
fo.close()
