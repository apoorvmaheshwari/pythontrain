fo=open('demo.txt','rb')
print("Cursor at ",fo.tell())
for line in fo:
	print(line.decode(),end="")
print("Cursor at ",fo.tell())
print("Reading again: ")	
fo.seek(0,0)
print("Cursor at ",fo.tell())
for line in fo:
	print(line.decode(),end="")
fo.close()