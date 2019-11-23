#!/usr/bin/python
import time
import datetime
print(datetime.datetime.now().time().isoformat())
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)