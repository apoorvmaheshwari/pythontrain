import re

pattern = '^t[a-z]*'
text = 'tom ,does this text match the pattern?'
matches=re.finditer(pattern,  text)
for match in matches:
	print(match.start(),
			match.end(),
			text[match.start():match.end()])

