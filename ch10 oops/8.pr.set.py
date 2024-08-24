# Write a class train which has method to book a ticket get status(no of seats) and get fare information of train running under india railway.

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def getStatus(self):
        print("*****************")
        print(f"the name of the train is {self.name}")
        print(f"the seats available in the train are {self.seats}")
        print("*****************")
    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry this train is full! kindly try in tatakal")


intercity = Train("Intercity Express: 14546", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()