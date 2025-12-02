""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
You = Hero("You", 350 , ["goldfish"])
You.buy({"title": "fishfood", "feed": 10})
print(You.__dict__)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")"""

class pet:
    def __init__(self, happiness, hunger, clean, age):
        self.happiness = happiness
        self.hunger = hunger
        self.clean = clean
        self.age = age
    def play(self):
        response = input(f"Do you want to play with {name2}? yes/no")
        while "yes" not in response and "no" not in response:
            print("Answer Invalid. Please Try Again")
            response = input(f"Do you want to play with {name2}?")
        if response == "yes":
            self.happiness += 5
            self.hunger -= 5
            self.clean -= 23
            print(f"{name2} is happy!")
        elif response == "no":
            self.happiness += 0
        else: 
            print("Answer Invalid. Please Try Again")

        if goldfish.clean > 100:
            goldfish.clean = 100
        if goldfish.clean < 0:
            goldfish.clean = 0
        if goldfish.happiness > 100:
            goldfish.happiness = 100
        if goldfish.happiness < 0:
            goldfish.happiness = 0

    def feed(self):
        response2 = input(f"{name2}'s getting hungry... Would you like to feed them? yes/no")
        while "yes" not in response2 and "no" not in response2:
            print("Answer Invalid. Please Try Again")
            response2 = input(f"{name2}'s getting hungry... Would you like to feed them?")
        if response2 == "yes":
            self.happiness += 2
            self.hunger += 15
        elif response2 == "no":
            self.happiness += 0 
            self.hunger -= 30
        else: 
            print("Answer Invalid. Please Try Again")
        if goldfish.clean > 100:
            goldfish.clean = 100
        if goldfish.clean < 0:
            goldfish.clean = 0
        if goldfish.happiness > 100:
            goldfish.happiness = 100
        if goldfish.happiness < 0:
            goldfish.happiness = 0

    def tidy(self):
        response3 = input(f"{name2}'s getting dirty... Would you like to clean them? yes/no")
        while "yes" not in response3 and "no" not in response3:
            print("Answer Invalid. Please Try Again")
            response3 = input(f"{name2}'s getting dirty... Would you like to clean them?")
        if response3 == "yes":
            self.happiness += 10
            self.hunger += 0
            self.clean += 20
        elif response3 == "no":
            self.happiness -= 5
            self.hunger += 0
            self.clean -= 35
        else: 
            print("Answer Invalid. Please Try Again")
        if goldfish.clean > 100:
            goldfish.clean = 100
        if goldfish.clean < 0:
            goldfish.clean = 0
        if goldfish.happiness > 100:
            goldfish.happiness = 100
        if goldfish.happiness < 0:
            goldfish.happiness = 0

    def status(self):
        response4 = input("It's the end of the day! Your goldfish is going to sleep. Would you like to see their stats?")
        while "yes" not in response4 and "no" not in response4:
            print("Answer Invalid. Please Try Again")
        if response4 == "yes":
            print(f"{name2}'s happiness is at {self.happiness}%. It's hunger is at {self.hunger}%. It's clean-ness is at {self.clean}%. Your pet is {self.age} days old.")
            self.age += 1
        else:
            self.age += 1

name = input("What's your name?")
print(f"Hi, {name}!")
name2 = input("what would you like to name your pet?")
goldfish = pet(70, 90, 95, 24)
print(f"Very nice! Meet your class pet, goldfish, {name2}. Take good care of them!")
while goldfish.age <= 70:
    goldfish.play()
    goldfish.feed()
    goldfish.tidy()
    goldfish.status()

    if goldfish.hunger > 125:
        print(f"{name2} died due to obesity :C")
        break
    elif goldfish.hunger < 10:
        print(f"{name2} died due to starvation :C")
        break
    elif goldfish.age > 50:
        print(f"{name2} died due to old age.")
        break
    



""" 
def verifyemail():
    email = input("What is your email?")
    password = input("What is your password?")
    if "@" not in email:
        return "not valid email"
    if any(char.isupper() for char in password) == False:
        return "inavlid password, needs at least 1 uppercase"
    if "@" in email and any(char.isupper() for char in password) == True:
        return "valid email and password!"
print(verifyemail()) """
