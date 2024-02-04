from ..observer.observer import Observer

class Samourai(Observer):
    def __init__(self):
        self.nom = ""
        self.force = 0
        self.arme = None
        self.dog = None

    # Accesseur pour l'arme du Samourai
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

    # Accesseurs pour le nouvel attribut 'nom'
    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    # Accesseurs pour le nouvel attribut 'force'
    def getForce(self):
        return self.force

    def setForce(self, force):
        self.force = force

    # Méthode pour augmenter la force du Samourai
    def augmenterForce(self, augmentation):
        self.force += augmentation

    def power(self):
        totalPower = self.force

        if self.arme is not None:
            totalPower += 2 * self.arme.getNiveau()

        return totalPower
    
    def computeTotalPower(self):
        return self.power()

    def setDog(self, dog):
        self.dog = dog
        dog.register_observer(self)

    # Nouvelle méthode pour nourrir le dog
    def feedDog(self, food):
        if self.dog is not None:
            self.dog.feed(food)

    # Implémentation de la méthode de l'observateur
    def update(self, state):
        print(f"{self.nom} observe : {state}")

    
