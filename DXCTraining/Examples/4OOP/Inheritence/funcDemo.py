class a:
	pass

a.name='SARAVAN'
class b(a):
	pass
print(b.__bases__[0].__dict__)

