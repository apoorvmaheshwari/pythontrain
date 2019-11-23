li=[
	{'fname':'Sachin' ,'lname': 'Tendulkar','team':'India' },
	{'fname':'Ricky' , 'lname':'Ponting','team':'Australia' },
	{'fname':'Rahul' , 'lname':'Dravid','team':'India' },
	{'fname':'Brian' , 'lname':'Lara','team':'West Indies' }
   ]
prepend="""<table border="1" style="color:red ; background-color:black">
		<thead>
		<th>Fname</th><th>Lname</th><th>Team</th>
		</thead>
		<tbody>"""
		
append=	"""</tbody></table>"""

temp="""<tr><td>{fname}</td><td>{lname}</td><td>{team}</td></tr>"""

 
report=''
report+=prepend
	
for el in li:
	data = temp.format(**el)
	report+=data
report+=append
	
open('output.html','w').write(report)



















