class JustCounter:
	__secretCount = 0
	def count(self):
		self.__secretCount += 1
		print(self.__secretCount)
counter = JustCounter()
counter.count()
counter.count()
#print(counter.__secretCount) will give error
#print(JustCounter.__secretCount) will give error
counter._JustCounter__secretCount+=2
print(counter._JustCounter__secretCount)
counter.count()
counter.count()
