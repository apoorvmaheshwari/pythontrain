li=[{'fname':'Sachin','lname':'Tendulkar','centuries':100},
{'fname':'Rahul','lname':'Dravid','centuries':88},
{'fname':'Saurav','lname':'Ganguly','centuries':62}]


li.sort(key=lambda d:d['fname'],reverse=True)