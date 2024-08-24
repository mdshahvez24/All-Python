import re 
  
print(re.findall(r'[Gg]eeks', 'GeeksforGeeks: \
A computer science portal for geeks'))


import re 
string = """Hello my Number is 123456789 and 
            my friend's number is 987654321"""
regex = '\d+'
  
match = re.findall(regex, string) 
print(match) 


# The code uses a regular expression pattern [a-e] to find and list all lowercase letters from ‘a’ to ‘e’ in the input string “Aye, said Mr. Gibenson Stark”. The output will be ['e', 'a', 'd', 'b', 'e'], which are the matching characters.

import re 
p = re.compile('[a-e]') 
  
print(p.findall("Aye, said Mr. Gibenson Stark")) 

# The code uses a regular expression pattern ‘ab*’ to find and list all occurrences of ‘ab’ followed by zero or more ‘b’ characters in the input string “ababbaabbb”.

import re 
p = re.compile('ab*') 
print(p.findall("ababbaabbb")) 