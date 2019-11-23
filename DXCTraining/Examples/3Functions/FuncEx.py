class sayHelloClass:
 def __call__(self,a):
  print("Hello %s"%a)

class modifySayHelloClass:
 def modifier(sayHelloObject,para)
  def innerMod(sayHelloObject,para)
   print("We are going to call sayHello")
   sayHelloObject(para)
   print("We just called SayHello")
 return(innerMod(sayHelloObject))


sayHello =sayHelloClass()
sayHello("PYTHON")
someThing=modifySayHelloClass.modifier(sayHello,para)
print(type(someThing))