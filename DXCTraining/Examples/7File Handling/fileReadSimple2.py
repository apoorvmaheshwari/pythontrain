fo = open("my.txt", "r")
data=fo.readlines()#list of lines
print(data)
print(type(data))#list
fo.close()
#_____________________________________

with open("my.txt", "r") as fo:
	for line in fo:
		print(line)
