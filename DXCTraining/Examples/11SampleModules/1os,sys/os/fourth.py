import os.path
print(os.environ['PYTHONPATH'])
os.environ['User']="root"
varPath='usr/$User/appdata'
actPath=os.path.expandvars(varPath)
print(actPath)






'''
The expandvars function inserts environment variables into a filename:

import os

os.environ["USER"] = "user"

print os.path.expandvars("/home/$USER/config")
print os.path.expandvars("$USER/folders")
'''