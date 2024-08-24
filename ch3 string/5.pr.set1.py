#WAP display a user entered name followed by good afternoon using input function

name = input("Enter your name \n")
print("Good aftrnoon," + name)

# WAP to detect double spaces in a String

st = "My name is Ali and i have to detect double   spaces in string"
doubleSpaces = st.find("  ")
print(doubleSpaces)

# WAP to repace doubleSpaces with single spacest 
st = "this is a string with double  spaces in string"

st = st.replace("  ", " ")
print(st)

# WAP to format the following letter
letter = "Dear harry this Python course is nice Thanks!"

formatted_letter = "Dear harry \n\tthis Python course is nice!\n Thanks!"
print(formatted_letter)