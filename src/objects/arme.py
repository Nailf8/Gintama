class Arme:
    def __init__(self):
        self.nom = ""
        self.niveau = 0
        self.samourai = None

    def setSamourai(self, samourai):
        self.samourai = samourai
        if samourai is not None and samourai.arme != self:
            samourai.setArme(self)

    # Accesseur pour le nom de l'arme
    def getNom(self):
        return self.nom

    # Mutateur pour le nom de l'arme
    def setNom(self, nom):
        self.nom = nom

    # Accesseur pour le niveau de l'arme
    def getNiveau(self):
        return self.niveau

    # Mutateur pour le niveau de l'arme
    def setNiveau(self, niveau):
        self.niveau = niveau
