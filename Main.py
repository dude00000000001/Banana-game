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
    

def mainMenu():
    print("Welcome to Banana farming.\n")
    print("Start [1]")
    print("Exit [2]\n")

    choice = input("Make your choice: ")

    if choice == "1":
        namePick()
    elif choice == "2":
        return
    else:
        print(f'{choice} was not an option. \n')
        mainMenu()

def namePick():
    print('')
    name = input("Please enter your name before you get started: ")
    player = Player(name)
    gameMenu(player)

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
        travelMenu()
    elif choice == "2":
        workerMenu()
    elif choice == "3":
        work()
    elif choice == "4":
        exchangeBananaMenu()
    elif choice == "5":
        exchangeCurrencyMenu()
    elif choice == "6":
        exit
    else:
        print(f'{choice} was not an option. \n')
        mainMenu()

def travelMenu():
    pass

def workerMenu():
    pass

def work():
    pass

def exchangeBananaMenu():
    pass

def exchangeCurrencyMenu():
    pass

    
mainMenu()

        
