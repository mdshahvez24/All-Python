# .format
w ="Welcome {} to Accenture {}".format("Ali",2023)
print(w) #Welcome Ali to Accenture 2023

w ="Welcome {0} to Accenture {1} we are greatful for you {2}".format("Ali",2023,"Mr.ALI")
print(w)  # Welcome Ali to Accenture 2023 we are greatful for you Mr.ALI

w ="Welcome {a} to Accenture {b}".format(a="Ali",b=2023)
print(w) #Welcome Ali to Accenture 2023

# spacing {a:10}
w ="Welcome {a:10} to Accenture {b}".format(a="Ali",b=2023)
print(w) #Welcome Ali        to Accenture 2023

# < for left spacing
w ="Welcome {a:>10} to Accenture {b}".format(a="Ali",b=2023)
print(w) #Welcome         Ali to Accenture 2023
#  > for right spacing
w ="Welcome {a:<10} to Accenture {b}".format(a="Ali",b=2023)
print(w) #Welcome Ali        to Accenture 2023
