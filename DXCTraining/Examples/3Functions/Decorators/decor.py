
def decorGenerator(someFunction):
 def inner():
  print(someFunction())
  return  "Inner was called"
 return inner

	
@decorGenerator
def getData():
 return "getData was called"

def getData2():
 return "getData2 was called"
 
print(getData())