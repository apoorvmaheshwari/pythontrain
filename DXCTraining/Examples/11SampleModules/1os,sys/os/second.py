import os
os.makedirs("test/multiple/levels")
os.removedirs("test/multiple/levels")
os.remove(filename)


# os.mkdir("test")
# os.rmdir("test")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#............................................

# where are we?
cwd = os.getcwd()
print "1", cwd

# go down
os.chdir("samples")
print "2", os.getcwd()

# go back up
os.chdir(os.pardir)
print "3", os.getcwd()

#,..............................................


os.makedirs("test/multiple/levels")
os.removedirs("test/multiple/levels")
os.remove(filename)


os.mkdir("test")
os.rmdir("test")

os.rmdir("someDirecotry") # this will fail if directory not empty

os.stat('filename') # if not working import stat

os.system('echo "hi"')

print os.name

#..............................................................
#os.path
print("using", os.name, "...")
print("split", "=>", os.path.split(filename))
print("splitext", "=>", os.path.splitext(filename))
print("dirname", "=>", os.path.dirname(filename))
print("basename", "=>", os.path.basename(filename))

 print file, "=>",
    if os.path.exists(file):
        print "EXISTS",
    if os.path.isabs(file):
        print "ISABS",
    if os.path.isdir(file):
        print "ISDIR",
    if os.path.isfile(file):
        print "ISFILE",
    if os.path.islink(file):
        print "ISLINK",
    if os.path.ismount(file):
        print "ISMOUNT",
		
The expandvars function inserts environment variables into a filename:

import os

os.environ["USER"] = "user"

print os.path.expandvars("/home/$USER/config")
print os.path.expandvars("$USER/folders")