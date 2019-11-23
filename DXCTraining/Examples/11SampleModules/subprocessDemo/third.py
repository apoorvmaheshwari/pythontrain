import subprocess
process1 = subprocess.Popen('dir', 
	shell=True,
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE )
process1.wait()
process2=subprocess.Popen('findstr "first"', 
	shell=True,
	stdin=process1.stdout,
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE 
	)
process2.wait()
for line in process2.stdout:
    print(line.decode())

