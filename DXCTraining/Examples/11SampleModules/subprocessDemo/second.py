import subprocess
def runcmd(cmd):
    x = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return x.communicate()

print(runcmd(input('Enter command to execute:'))[0].decode())




'''
data= runcmd("dir")
for line in data:
	print(line.decode())
'''