temp='Hello {title}.{name} ,How are you ?'
d={'title':'Mr' , 'name':'Sachin'}
data=temp.format(**d)
print(data)