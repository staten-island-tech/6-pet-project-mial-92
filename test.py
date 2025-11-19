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
        print(f"{self.owner} has ${self.__balance}")

class pet:
    def __init__(pet, happiness, hunger, clean, age):
        pet.__happiness = happiness
        pet.__hunger = hunger
        pet.__clean = clean
        pet.__age = age
    def play(pet):
        pet.__happiness = 75
        response = input(f"Do you want to play with {pet_name}?")
        if response == "yes" in response:
            pet.__happiness += 5
            pet.__hunger -= 5
            pet.__clean -= 12
            print(f"{pet_name} is happy!")
        elif response == "no":
            pet.__happiness += 0
        else: 
            print("Answer Invalid. Please Try Again")
        if pet.__happiness > 100:
            pet.__happiness = 100
        if pet.__clean > 100:
            pet.__clean = 100
    def feed(pet):
        pet.__hunger = 100
        response2 = input(f"{pet_name}'s getting hungry... Would you like to feed them?")
        if response2 == "yes" in response2:
            pet.__happiness += 2
            pet.__hunger += 5
            pet.__clean -= 10
        elif response2 == "no" in response2:
            pet.__happiness += 0 
            pet.__hunger -= 8
            pet.__clean += 0
        else: 
            print("Answer Invalid. Please Try Again")
        if pet.__happiness > 100:
            pet.__happiness = 100
        if pet.__clean > 100:
            pet.__clean = 100
    def clean(pet):
        pet.__clean = 100
        response3 = input(f"{pet_name}'s getting dirty... Would you like to clean them?")
        if response3 == "yes" in response3:
            pet.__happiness += 10
            pet.__hunger += 0
            pet.__clean += 20
        elif response3 == "no" in response3:
            pet.__happiness -= 5
            pet.__hunger += 0
            pet.__clean -= 10
        else: 
            print("Answer Invalid. Please Try Again")
        if pet.__happiness > 100:
            pet.__happiness = 100
        if pet.__clean > 100:
            pet.__clean = 100
name = input("What's your name?")
print(f"Hi, {name}!")
pet_name = input("what would you like to name your pet?")
print(f"Very nice! Meet your class pet, goldfish, {pet_name}. Take good care of them!")
input(f"Do you want to play with {pet_name}?")

class pet:
    def __init__
        animal.happiness = happiness
        animal.hunger = hunger
        animal.clean = clean
    def deposit(animal, happiness):
        animal._balance1 += happiness
    def deposit(animal, hunger):
        animal._balance2 += hunger
    def deposit(animal, clean):
        animal._balance3 += clean

    def show_balance(pet_name):
        print(f"{pet_name} is at {animal._balance1}% happiness")  """

def verifyemail():
    email = input("What is your email?")
    password = input("What is your password?")
    if "@" not in email:
        return "not valid email"
    if any(char.isupper() for char in password) == False:
        return "inavlid password, needs at least 1 uppercase"
    if "@" in email and any(char.isupper() for char in password) == True:
        return "valid email and password!"
print(verifyemail())
