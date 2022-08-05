# Parent Class : User
# Holds details about user
# Has a function to show user details
# Child Class : Bank
# Stores details about the account balance
# Stores details about the amount
# Allows for deposits, withdraws, view_balance

# Parent Class
class User:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)


# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print ("Account balance has been udpated $: ", self.balance)
