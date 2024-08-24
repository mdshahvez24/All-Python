# Create a class programmer for storing information of few programmer working at  microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"the name of the {self.company} programmer is {self.name} and the product is {self.product}")

harry = Programmer("harry", "skype")
alka = Programmer("alka", "github")
harry.getInfo()
alka.getInfo()
        