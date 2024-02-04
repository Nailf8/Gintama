import unittest
from samourai import Samourai
from arme import Arme

class SamouraiTest(unittest.TestCase):

    def setUp(self):
        self.arme = Arme('boken')
        self.samourai = Samourai('Gintoki')
        self.samourai.setPower(70)
        self.arme.setLvl(20)
        self.samourai.setArme(self.arme)

    def testAugmenterForce(self):
        self.samourai.improvePower(20)
        self.assertEqual(90, self.samourai.getPower())

    def testFixture(self):
        # Add your fixture test code here
        pass

    def testAssociationBidirectionnelle(self):
        self.assertEqual(self.samourai, self.arme.samourai)
        self.assertEqual(self.arme, self.samourai.arme)

        self.samourai.removeArme()
        self.assertIsNone(self.arme.samourai)
        self.assertIsNone(self.samourai.arme)

if __name__ == '__main__':
    unittest.main()
