import re
s = "string. With. Punctuation?"
s = re.sub(r'[^\w\s]','',s)

print(s)