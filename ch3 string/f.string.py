letter ="hey my name is {1} and I am from {0}"
country="India"
name="ALi"

# print(letter.format(name,country))
print(letter.format(country,name,))

print(f"hey my name is {name} and I am from {country}")

price = 49.9998
txt =f"for only {price:2f} dollars!"
print(txt)
# print(txt.format())