with open("my.txt", "rb") as fo:
	for line in fo:
		print(line.decode())
	print(fo.tell())
	fo.seek(-10,2)
	print(fo.tell())
	print("Reading Again:")
	for line in fo:
		print(line.decode())
