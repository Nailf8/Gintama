class Arme:
    def __init__(self, name):
        self.name = name
        self.lvl = 0
        self.samourai = None

    def setSamourai(self, samourai):
        self.samourai = samourai
        if samourai is not None and samourai.arme != self:
            samourai.setArme(self)

    def getLvl(self):
        return self.lvl

    def setLvl(self, niveau):
        self.niveau = niveau
