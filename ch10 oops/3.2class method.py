class Mobile:
    @classmethod            # decorator
    def show_model(cls):    # class Method
        print("Realme X") 

realme=Mobile()
Mobile.show_model()  # calling class method

# class methid is use when we r working with variable

class Mobile:
    fp= 'yes'   # class variable
    @classmethod
    def show_model(cls):
        print("Fingrprint :", cls.fp)

realme = Mobile()
Mobile.show_model()

# with arguments
class Mobile:
    fp= 'yes'   # class variable
    @classmethod
    def show_model(cls, r):
        cls.ram=r
        print("Fingrprint :", cls.fp)
        print("RAM:", cls.ram)

realme = Mobile()
Mobile.show_model('4GB')
