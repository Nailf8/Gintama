import unittest
from package.dog import Dog  
from package.samourai import Samourai


class DogTest(unittest.TestCase):
    def setUp(self):
        self.dog = Dog('Buddy')
        self.samourai = Samourai('Gintoki')

    def testInitialSatisfaction(self):
        self.assertFalse(self.dog.is_satisfied())

    def testFeedDog(self):
        food = 'dog food'
        self.dog.feed(food)
        self.assertTrue(self.dog.is_satisfied())

    def testObserverRegistration(self):
        self.dog.register_observer(self.samourai)
        self.assertIn(self.samourai, self.dog._observers)

    def testObserverUnregistration(self):          
        self.dog.register_observer(self.samourai)
        self.dog.unregister_observer(self.samourai)
        self.assertNotIn(self.samourai, self.dog._observers)



if __name__ == '__main__':
    unittest.main()
