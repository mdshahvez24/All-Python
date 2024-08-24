class Mobile:
    fp= 'yes'   # class variable
    @classmethod
    def is_fp(cls):
        print("Fingrprint :", cls.fp)

realme = Mobile()
redmi = Mobile()
Moto = Mobile()

print("Class Fp:", Mobile.fp)  # yes all
print("Realme Fp:", realme.fp)
print("Redmi Fp:", redmi.fp)
print("Moto Fp:", Moto.fp)  # yes all

print('')
Mobile.fp = 'No'
print("Realme Fp:", realme.fp) # all NO
print("Redmi Fp:", redmi.fp)
print("Moto Fp:", Moto.fp)

realme.fp='not working'
print("Class Fp:", Mobile.fp) 
print("Realme Fp:", realme.fp)  #not working only
print("Redmi Fp:", redmi.fp)
print("Moto Fp:", Moto.fp) 
