from xmlrpc.client import FastParser


class Plant:
    def (self, watered, alive, fruit):
        self.beenWatered = watered
        self.isAlive = alive
        self.hasFruit = fruit

class Racoon:
    def __init__(self, eats):
        self.hasEaten = eats

class Human:
    def __init__(self, waters, picks):
        self.isWatering = waters
        self.isPicking = picks

plant1 = Plant()
plant1.beenWatered = False
print(plant1.beenWatered) 



