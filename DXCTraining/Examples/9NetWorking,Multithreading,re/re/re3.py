import re

pattern = '^t\S*|\st\S*'
text = 'Tom Does this and tom   match that team this  pattern? tom123'

matches = re.findall(pattern, text,re.IGNORECASE)
#matches is list of matching strings
print(matches)