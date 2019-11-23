mytuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print mytuple           # Prints complete list
print mytuple[0]        # Prints first element of the list
print mytuple[1:3]      # Prints elements starting from 2nd till 3rd 
print mytuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints tuple two times
print mytuple + tinytuple # Prints concatenated tuple
mytuple.append(10)
print mytuple