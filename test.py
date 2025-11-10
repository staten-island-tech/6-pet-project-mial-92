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
 """
name = input("What's your name?")
print(f"Hi, {name}!")
pet_name = input("what would you like to name your pet?")
print(f"Very nice! Meet your class pet, goldfish, {pet_name}. Take good care of them!")

class pet:
    def __init__(pet, animal, happiness, hunger, clean):
        pet._happiness = happiness
        pet._hunger = hunger
        pet._clean = clean
    def play(pet, happiness):
        happiness = 75
        response = input(f"Do you want to play with {pet_name}?")
        if "yes" in response:
            happiness += 5
            hunger -= 5
            clean -= 10
            print(f"{pet_name} is happy!")
        elif "no":
            happiness += happiness
        else:
            print("Answer Invalid. Please Try Again")

""" class pet:
    def __init__(animal, happiness, hunger, clean):
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
        print(f"{pet_name} is at {animal._balance1}% happiness") """