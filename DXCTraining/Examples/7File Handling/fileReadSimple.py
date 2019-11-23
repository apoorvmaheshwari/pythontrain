fo = open("my.txt", "r")
data=fo.read()
print(data)
fo.close()
#_____________________________________

fo = open("my.txt", "r")
data=fo.read(10)#first 10 bytes
print(data)
data=fo.read(10)#next 10bytes
print(data)
data=fo.read(10)#next 10bytes
print(data)
fo.close()
#_____________________________________
		
fo = open("my.txt", "r")
data=fo.readline()#first line
print(data)
data=fo.readline()#second line
print(data)
data=fo.readline()#third line
print(data)
fo.close()