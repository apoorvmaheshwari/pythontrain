import os
for filenames in os.listdir():
    print(filenames)
print(os.getcwd())
os.chdir('D:\Python')
print(os.getcwd())
	