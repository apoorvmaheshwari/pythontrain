fo = open("my.txt", "r")
it=iter(fo)
print(type(it))
for line in fo:
		print(line)

for line in fo:
		print(line)

print('*****************************************************************')	
fo.seek(0,0)
for line in fo:
		print(line)



print(fo.tell())
fo.close()
		
'''
		
st='we are  are talking about talking talking file reading'
d={}
for l in st.split():
	if l in list(d.keys()):
		d[l]+=1
	else:
		d[l]=1
'''