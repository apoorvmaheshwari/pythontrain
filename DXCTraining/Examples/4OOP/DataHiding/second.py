class JustCounter:
	__secretCount = 0
	def count(self):
		JustCounter.__secretCount += 1
		print(JustCounter.__secretCount)
counter = JustCounter()
counter.count()
counter.count()
counter._JustCounter__secretCount+=2
print(counter._JustCounter__secretCount)
counter.count()
counter.count()
#print(counter.__secretCount) will give error
#print(JustCounter.__secretCount) will give error



