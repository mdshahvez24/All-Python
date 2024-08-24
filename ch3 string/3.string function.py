#   .lower() -- change character to lower case
w = "I am a Software Engg"
n=w.lower()
print(n) #  i am a software engg

# .upper() change into upper case 
u = "i am a software engg"
n = u.upper()
print(n) #I AM A SOFTWARE ENGG

# .title() change only first letter of charater into upper case
t="I am a Software Engg"
t=t.title()
print(t)  #I Am A Software Engg

# .capitalize() -only first letter capital all small

c = "I Am a Software engg"
n = c.capitalize()
print(n)

# chr() to get out put in charcter
a = 66  #65 A 66 B  67 C
print(chr(a))

# ord() to get out put in integer nd pass  charater

o = "A"
print(ord(o))  # 65

story = "once upon a time there was a youtuber named harry  who uploaded python course with notes harry"

 # string function
print(len(story))
print(story.endswith("notes"))
print(story.count("a"))  # character occurence
print(story.count("course"))  
print(story.count("c"))  
print(story.capitalize())  # capitalize the first character
print(story.find("harry"))
print(story.replace("harry", "shahvez")) #replace all harry word of a string by shahvez
