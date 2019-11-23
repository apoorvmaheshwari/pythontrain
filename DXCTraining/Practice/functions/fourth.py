#var length keyworded args
def sayhi(**kwargs):
	print(type(kwargs),kwargs)


sayhi(name1='Sachin')
sayhi(name1='Sachin',name2='Saurav')
sayhi(name1='Sachin',
		name2='Saurav',name3='Rahul')