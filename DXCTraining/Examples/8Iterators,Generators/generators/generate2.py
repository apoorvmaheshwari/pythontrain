def MyGen(uL):
	i=0
	while(i<len(uL.li)):
		if(uL.li[i].ps>50):
			yield uL.li[i].id 
		i+=1
class user:
	uid=0
	ps=0
	def __init__(self,ps):
		user.uid+=1
		self.id=user.uid
		self.ps=ps
class userList:
	li=[]
userList.li.append(user(60))
userList.li.append(user(10))
userList.li.append(user(90))
userList.li.append(user(30))
userList.li.append(user(500))

for x in  MyGen(userList):
	print(x)