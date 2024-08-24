# WAP to fill in a letter template given below with name nd date
# letter = '''Dear <|name|>
# you are selected
# <|date|>'''

letter = '''Dear <|NAME|>,
Greeting from abc coding house. I am happy to tell you abt your selesction. 
You are selected!
Have a great day ahead!
thanks and regards,
Seven
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)