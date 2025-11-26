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
        self.__happiness = happiness
        self.__hunger = hunger
        self.__clean = clean
        self.age = age
    def play(self):
        response = input(f"Do you want to play with {name2}?")
        if response == "yes" in response:
            self.__happiness += 5
            self.__hunger -= 5
            self.__clean -= 12
            print(f"{name2} is happy!")
        elif response == "no":
            self.__happiness += 0
        else: 
            print("Answer Invalid. Please Try Again")

    def feed(self):
        response2 = input(f"{name2}'s getting hungry... Would you like to feed them?")
        if response2 == "yes" in response2:
            self.__happiness += 2
            self.__hunger += 5
            self.__clean -= 10
        elif response2 == "no" in response2:
            self.__happiness += 0 
            self.__hunger -= 8
            self.__clean += 0
        else: 
            print("Answer Invalid. Please Try Again")

    def clean(self):
        response3 = input(f"{name2}'s getting dirty... Would you like to clean them?")
        if response3 == "yes" in response3:
            self.__happiness += 10
            self.__hunger += 0
            self.__clean += 20
        elif response3 == "no" in response3:
            self.__happiness -= 5
            self.__hunger += 0
            self.__clean -= 10
        else: 
            print("Answer Invalid. Please Try Again")

    def status(self):
        answer4 = input("It's the end of the day! Your goldfish is going to sleep. Would you like to see their stats?")
        if answer4 == "yes":
            print(f"{name2}'s happiness is at {self.__happiness}%. It's hunger is at {self.__hunger}%. It's clean-ness is at {self.__clean}%. Your pet is {self.age} years old.")
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
    goldfish.clean()
    goldfish.status()
    if goldfish.__hunger > 125:
        print(f"{name2} died due to obesity :C")
        break
    elif goldfish.__hunger > 10:
        print(f"{name2} died due to starvation :C")
        break
    elif goldfish.age > 70:
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
