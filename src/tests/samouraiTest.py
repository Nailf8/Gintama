import unittest
from Samourai import Samourai
from Arme import Arme 

class SamouraiTest(unittest.TestCase):

    def setUp(self):
        arme = Arme()
        self.bokken = arme
        self.Gintoki = Samourai()
        self.Gintoki.setForce(70)
        self.Gintoki.setNom("Gintoki")
        self.bokken.setNiveau(20)
        self.Gintoki.getArme()
        self.Gintoki.calculerPuissanceTotale()

    def testAugmenterForce(self):
        self.Gintoki.setForce(100)

        self.Gintoki.augmenterForce(20)

        self.assertEqual(120, self.Gintoki.getForce())

    def testChangerNom(self):
        self.Gintoki.setNom("Hattori Hanzo")

        self.Gintoki.setNom("Yamada Jiro")

        self.assertEqual("Yamada Jiro", self.Gintoki.getNom())

    def testFixture(self):
        pass

    def testAssociationBidirectionnelle(self):
        arme = Arme()

        self.Gintoki.setArme(arme)
        self.assertEqual(self.Gintoki, arme.samourai)
        self.assertEqual(arme, self.Gintoki.arme)

        self.Gintoki.removeArme()
        self.assertIsNone(arme.samourai)
        self.assertIsNone(self.Gintoki.arme)


if __name__ == '__main__':
    unittest.main()
