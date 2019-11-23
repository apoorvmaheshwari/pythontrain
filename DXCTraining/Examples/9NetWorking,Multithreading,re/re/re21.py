import re

pattern = '^t\w*\s|\st\w*\s|\st\w*'
text = ' Does this and tom   match that team   pattern? tom123'

li = re.finditer(pattern, text)
for e in li:
	print(e.start(),e.end(),text[e.start():e.end()])
