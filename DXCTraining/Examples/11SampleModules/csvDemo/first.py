import csv
reader = csv.reader(open('demo.csv','r'),delimiter=',')
for data in reader:
	print(data)
