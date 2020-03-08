import random

class Player:

    def __init__(self,name):
        self._name = name
        self._bananas = 10
        self._money = 500
        self._workers = []
        self._location = "United States"
        self._currency = "USD"

    def name (self):
        return self._name

    def bananas (self):
        return self._bananas

    def money (self):
        return self._money

    def workers (self):
        return self._workers

    def location (self):
        return self._location

    def currency(self):
        return self._currency

    def relocate(self,country,current):
        with open("travel.txt") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                if country in line and current in line:
                    if line[2] == "(water)":
                        return True
                    return False
    

def mainMenu():
    print('')
    print("Welcome to Banana farming.\n")
    print("Start [1]")
    print("Exit [2]\n")

    choice = input("Make your choice: ")

    if choice == "1":
        namePick()
    elif choice == "2":
        return
    else:
        print(f'{choice} was not an option.')
        mainMenu()

def namePick():
    print('')
    name = input("Please enter your name before you get started: ")
    player = Player(name)
    gameMenu(player)
    return

def gameMenu(player):
    print('')
    print(f'{player.name()}, you are in {player.location()}, have {player.bananas()} bananas, and have {player.money()} {player.currency()}.\n')

    print("Travel [1]")
    print("Manage workers [2]")
    print("Farm bananas [3]")
    print("Exchange money for bananas [4]")
    print("Exchange currency [5]")
    print("Quit [6]\n")

    choice = input("Make your choice: ")

    if choice == "1":
        travelMenu(player)
    elif choice == "2":
        workerMenu(player)
    elif choice == "3":
        work(player)
    elif choice == "4":
        exchangeBananaMenu(player)
    elif choice == "5":
        exchangeCurrencyMenu(player)
    elif choice == "6":
        return
    else:
        print(f'{choice} was not an option.')
    gameMenu(player)

def travelMenu(player):
    locations = ["United States", "Ecuador", "Russia", "Philippines", "Guatemala", "Belgium"]

    print('')
    print("Please select a country to travel to.\n")

    for i in range (len(locations)):
        if locations[i] != player.location():
            print(f'{locations[i]}')
    
    print("\nExit [0]\n")

    choice = input("Make your choice (enter a country EXACTLY as it appears): ")

    if choice in locations and choice != player.location():
        travel(player,choice,player.location())
    elif choice == "0":
        return
    else:
        print(f'{choice} was not an option.')
    travelMenu(player)

def travel(player,destination,current):
    chance = player.relocate(destination,current)

    print(chance)

    
def workerMenu():
    pass

def work():
    pass

def exchangeBananaMenu():
    pass

def exchangeCurrencyMenu():
    pass

    
mainMenu()

        
