from observer.observer import Observer

class Samourai(Observer):
    def __init__(self, name):
        self.name = name
        self.power = 0
        self.arme = None
        self.dog = None

    def getArme(self):
        return self.arme

    def setArme(self, arme):
        if self.arme is not None:
            raise ValueError("le samourai a déjà une arme")
        self.arme = arme
        arme.setSamourai(self)

    def removeArme(self):
        if self.arme is not None:
            arme = self.arme
            self.arme = None
            arme.setSamourai(None)

    def getPower(self):
        return self.power

    def setPower(self, power):
        self.power = power

    def improvePower(self, augmentation):
        self.power += augmentation

    def computeTotalPower(self):
        totalPower = self.power

        if self.arme is not None:
            totalPower += 2 * self.arme.getLvl()

        return totalPower

    def setDog(self, dog):
        self.dog = dog
        dog.register_observer(self)

    def feedDog(self, food):
        if self.dog is not None:
            self.dog.feed(food)

    # Implement observer method
    def update(self, state):
        print(f"{self.name} observe : {state}")

    
