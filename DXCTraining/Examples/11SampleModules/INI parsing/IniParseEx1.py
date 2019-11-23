import configparser
config = configparser.ConfigParser()
config.read('examples.ini')
print('Sections in the INI File : ',config.sections())
print('bitbucket.org' in config)
print('bytedata.com' in config )

print(config['bitbucket.org']['User'])
print(config['DEFAULT']['Compression'])
topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(topsecret['Port'])


print("The for Loop:")
bigbuck=config['bitbucket.org']
for key in bigbuck:
 print(key,'==',bigbuck[key])
default=config['DEFAULT']
print(config['bitbucket.org']['Compression'])
