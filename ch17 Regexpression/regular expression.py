# Regular Expression --  Regex is a special sequence of character that uses a search pattern tofind a string or set of string.

# It can detect the presence or absence of a text by matching it by with particular pattern and can split a pattern into one or more sub pattern 

import re

pattern = r"[A-Z]+yclone"

text = '''
Welcome! Are you completely new to programming? If not then we presume you will be looking for information about why and how to Cyclone get started with Python. Fortunately an experienced programmer in any programming language (whatever it may be) Dyclone can pick up Python very quickly. It's also easy for beginners to use and learn, so jump in!


'''

# re.search() it stop on first match
# match = re.search(pattern, text)
# print(match)
 
matches = re.finditer(pattern,text)
for match in matches:
    print(match)
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
    