# Default order 
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 
  
# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 
  
# Keyword Formatting 
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life') 
print("\nPrint String in order of Keywords: ") 
print(String1) 



# A Python program to demonstrate the 
# working of the string template 
from string import Template 
  
# List Student stores the name and marks of three students 
Student = [('Ram',90), ('Ankit',78), ('Bob',92)] 
  
# We are creating a basic structure to print the name and 
# marks of the students. 
t = Template('Hi $name, you have got $marks marks') 
  
for i in Student: 
     print (t.substitute(name = i[0], marks = i[1])) 