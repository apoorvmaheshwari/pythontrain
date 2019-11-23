import tempfile,shlex
tf = tempfile.NamedTemporaryFile(delete=False)
tf.write('Some data')
tfname= tf.name
print tfname
tf.close()
#tfname=tfname.replace('\\','\\\\')
print 'After Replace:'+tfname
cmdlet= 'hdbsql -U {userkey} -amxj -I {f}'
cmdf=cmdlet.format(userkey='ABCDEF', f=tfname )
print cmdf
cmdshlex= shlex.split(cmdf,posix=False)
print cmdshlex