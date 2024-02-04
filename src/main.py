from objects.dog import Dog
from objects.samourai import Samourai


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un chien et d'un samouraï
    dog = Dog("Sadaharu")
    samourai = Samourai()
    samourai.setNom('Gintoki')
    samourai.setDog(dog)

    # Le samouraï nourrit le chien
    dog.feed("viande")