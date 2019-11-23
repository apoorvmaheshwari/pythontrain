dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales','name':'Tom'}


print dict['one']       # Prints value for 'one' key
print dict 
print tinydict['name']           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print list(tinydict.keys())   # Prints all the keys
print tinydict.values() # Prints all the values