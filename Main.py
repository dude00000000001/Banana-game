import random

class Player:

    def __init__(self,name):
        self._name = name
        self._bananas = 10
        self._money = 200
        self._location = "United States"
        self._currency = "USD"

    def name (self):
        return self._name

    def bananas (self):
        return self._bananas

    def money (self):
        return f'{self._money:.2f}'

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
                    self._location = country
                    if line[2] == "(water)":
                        return True
                    return False

    def turbulence (self):
        with open ("currency.txt") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                if line[2] == self._currency:
                    self._money = self._money - 100 * float(line[1])
                    if self._money < 0:
                        self._money = 0
                    return

    def work (self):
        with open ("payoff.txt") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                if line[0] == self._location:
                    material = random.randint(int(line[1]),int(line[2]))
                    return material

    def addBananas(self,adding):
        self._bananas += adding

    def currencyCheck(self):
        with open ("currency.txt") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                if line[0] == self._location:
                    if self._currency == line[2]:
                        return True
                    return False

    def bananasToMoney(self,bananas,cost):
        moneyGain = bananas * cost
        self._bananas -= bananas
        self._money += moneyGain

    def moneyToBananas(self,bananas,cost):
        moneyLoss = bananas * cost
        self._bananas += bananas
        self._money -= moneyLoss
                    
    
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
    print("Farm bananas [2]")
    print("Exchange money for bananas [3]")
    print("Exchange currency [4]")
    print("Quit [5]\n")

    choice = input("Make your choice: ")

    if choice == "1":
        travelMenu(player)
    elif choice == "2":
        work(player)
    elif choice == "3":
        exchangeBananaMenu(player)
    elif choice == "4":
        exchangeCurrencyMenu(player)
    elif choice == "5":
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
        travel(player,choice)
    elif choice == "0":
        return
    else:
        print(f'{choice} was not an option.')
    travelMenu(player)

def travel(player,destination):
    chance = player.relocate(destination,player.location())

    if chance == True:
        luck = random.randint(1,2)
    else:
        luck = 2

    if luck == 1:
        player.turbulence()
        print(f'On your way to {player.location()}, you experienced turbulence that slowed down your travel. You lost 100 USD for arriving late, and now have {player.money()} {player.currency()}. If you did not have that much, you lost all your money.')
    input(f'You have arrived in {player.location()}. Press any key to continue.')
    return


def work(player):
    workload = player.work()
    player.addBananas(workload)

    print(f'You successfully farmed {workload} bananas today. You now have {player.bananas()} bananas.\n')
    input("Press any key to continue.")
    return

def exchangeBananaMenu(player):
    correct = player.currencyCheck()
    if correct == True:
        print(f'{player.name()}, what type of exchange would you like to do?\n')

        print("Bananas -> Money [1]")
        print("Money -> Bananas [2]")
        print("Exit [3]\n")

        choice = input("Make your choice: ")

        if choice == "1":
            bananaToMoney(player)
        elif choice == "2":
            moneyToBanana(player)
        elif choice == "3":
            return
        else:
            print(f'{choice} was not an option.')
        exchangeBananaMenu(player)
    else:
        print(f'Your money is not in the correct currency for {player.location()}. Please visit the currency exchange menu.')
    return
    
def bananaToMoney(player):
    bananaPrice = costOfBanana(player.location())
    print(f'You have {player.bananas()} bananas and {player.money()} {player.currency()}. One banana will give you {bananaPrice} {player.currency()}.\n')

    try:
        amount = int(input("How many bananas would you like to sell: "))
    except ValueError:
        print("That is not a valid integer for bananas.")
        return

    if amount > player.bananas():
        print(f'You do not have {amount} bananas.\n')
    elif amount < 0:
        print("Negative bananas do not exist, dingus.")
    elif amount == 0:
        print("Why would you want to exchange no bananas? You get nothing in return.")
    else:
        player.bananasToMoney(amount,bananaPrice)
        print("Conversion successful!")
    return

def costOfBanana(country):
    with open("bananas.txt") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            if line[0] == country:
                return float(line[1])

def moneyToBanana(player):
    bananaPrice = costOfBanana(player.location())
    print(f'You have {player.bananas()} bananas and {player.money()} {player.currency()}. One banana will cost you {bananaPrice} {player.currency()}.\n')

    try:
        amount = int(input("How many bananas would you like to buy: "))
    except ValueError:
        print("That is not a valid integer for bananas.")
        return

    if amount < 0:
        print("Negative bananas do not exist, dingus.")
    elif amount == 0:
        print("Why would you want to buy no bananas? This costs you nothing.")
    elif float(amount * bananaPrice) > float(player.money()):
        print(f'You need {amount * bananaPrice:.2f} {player.currency()} to make this purchase. You have {player.money()} {player.currency()}.')
    else:
        player.moneyToBananas(amount,bananaPrice)
        print("Conversion successful!")
    return

def exchangeCurrencyMenu():
    pass

    
mainMenu()
