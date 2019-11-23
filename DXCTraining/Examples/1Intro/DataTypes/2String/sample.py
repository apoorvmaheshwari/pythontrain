def crit(d):
	return d['name']
dict1={'title':'Mr' , 'name':'Rahul','couponCode':'QWQASD2'}
dict2={'title':'Mrs' , 'name':'Radha','couponCode':'QWQASD2'}
dict3={'title':'Ms' , 'name':'Richa','couponCode':'QWQASD2'}
dict4={'title':'Mr' , 'name':'Sachin','couponCode':'QWQASD2'}
li=[dict1,dict2,dict3,dict4]

li.sort(key=crit,reverse=True)















template="Hi {title}. {name} , your discount coupon is {couponCode}"
for dt in li:
	print(template.format(**dt))
