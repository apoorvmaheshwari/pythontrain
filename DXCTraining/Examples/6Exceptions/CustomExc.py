class ShortInputException(Exception):
	'''A user-defined exception class.'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	a=2/0
	s =input('Enter something --> ')
	if len(s) < 3:
		raise ShortInputException(len(s), 3)
	# Other work can continue as usual here
except EOFError:
	print('EOF')
except ShortInputException as x:
	print('ShortInputException: The input was of length %d \n, \
		was expecting at least %d' % (x.length, x.atleast))
else:
	print('No exception was raised.')
finally:
	print('this is Finally')

print('rest of the code')


"""under age exception"""
				