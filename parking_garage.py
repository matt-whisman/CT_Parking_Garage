class parking_garage:
    def __init__(self):
        self.ticket_price = 2.5
        self.spaces = 100
        self.tickets = 100

    def taketicket(self):
        self.user_enter = input(
            "Welcome to the GARAGE, price is $2.50 would you like to park here y for yes: "
        ).lower()
        if self.user_enter == "y":
            self.tickets -= 1
            self.spaces -= 1
            userleave = input(
                "\nPark wherever you'd like, press any key when you'd like to leave: "
            )
            if userleave != "":
                self.pay()
        else:
            print("\nHave a nice day!")

    def pay(self):
        print(f"\nSwipe your card to pay {self.ticket_price}")
        swiped = input("\nPress y if you swiped your card: ").lower()
        while swiped != "y":
            swiped = input("\nYou must still pay! Press y if you swiped your card: ")
        print("\nYou have 15 minutes to leave, have a nice day!")
        self.leave()

    def leave(self):
        self.spaces += 1
        self.tickets += 1


car1 = parking_garage()
car1.taketicket()
