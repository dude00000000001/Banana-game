class Player:

    def __init__(self,name):
        self._name = name
        self._bananas = 10
        self._money = 500
        self._workers = []
        self._location = "United States"
        self._fairtrade = False

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

    def fairtrade (self):
        return self._fairtrade

    
