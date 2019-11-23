import re

pattern = '^t\S*|\st\S*'
text = 'Tom Does this and tom   match that team this  pattern? tom123'

matches = re.finditer(pattern, text,re.IGNORECASE)
for match in matches:
	print(match.start(),
			match.end(),
			text[match.start():match.end()])