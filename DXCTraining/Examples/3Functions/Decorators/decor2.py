
def decorGenerator(someFunction):
 def inner(name):
  print('invoking:'+someFunction.__name__)
  print(someFunction(name))
  return  someFunction.__name__+"was invoked"
 return inner

	
@decorGenerator
def getData(name):
 return "getData was called for"+name

def getData2():
 return "getData2 was called"
 
print(getData('Python'))