from abc import ABC, abstractmethod

# Classe abstraite pour les observateurs
class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

