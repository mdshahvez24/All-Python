# create a dictionary allow 4 friend to enter their fav language as value and use keys as their name  
favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
# favLang['shubham'] = a
# favLang['ankit'] = b
# favLang['sonali'] = c
# favLang['harshita'] = d

#If the name of 2 students are same   
favLang['shubham'] = a
favLang['ankit'] = b
favLang['shubham'] = c
favLang['harshita'] = d
print(favLang)

#  in a dictionary value are not be unique but unique keys needed