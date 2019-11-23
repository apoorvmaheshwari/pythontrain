from ConfigParser import SafeConfigParser
config = SafeConfigParser()
config.read('examples.ini')
"""
print('Sections in the INI File : ',config.sections())


print('config[\'bitbucket.org\'][\'User\']=',config.get('bitbucket.org', 'User'))
print('config[\'bitbucket.org\'][\'Compression\']=',config.get('bitbucket.org', 'Compression'))
print('config[\'DEFAULT\'][\'Compression\']=',config.get('DEFAULT', 'Compression'))

if 'bitbucket.org' in config.sections():
        print '[bitbucket.org] exists'
if config.has_option('bitbucket.org', 'User'):
    print 'USER exists in [bitbucket.org]'

print(config.get('DEFAULT','CompressionLevel'))
print config.options('bitbucket.org')
"""
try:
	az= config.get('DEFAULT','AAZZXX')
except Exception as e:
	az=''
print "This one:",az.split(',')
