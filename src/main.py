from package.samourai import Samourai
from package.dog import Dog
from package.arme import Arme

def main():
    # Create instances
    gintoki = Samourai('Gintoki')
    sadaharu = Dog('Sadaharu')
    boken = Arme('boken')

    # Set up associations
    gintoki.setDog(sadaharu)
    boken.setLvl(29)
    gintoki.setArme(boken)
    gintoki.setPower(40)
    

    # Test the observer pattern
    sadaharu.feed('meat')  # This should trigger the update method in Samourai

    # Test samurai's power
    print(f"{gintoki.name}'s total power: {gintoki.computeTotalPower()}")

    # Test forgetting to feed Sadaharu
    gintoki.feedDog('')  # This should lead to Sadaharu eating someone

if __name__ == "__main__":
    main()
