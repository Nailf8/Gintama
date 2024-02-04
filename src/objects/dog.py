class Dog:
    def __init__(self, name):
        self.name = name
        self.satisfied = False
        self._observers = []  # Liste des observateurs (samouraïs)
    
    def is_satisfied(self):
        return self.satisfied

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, state):
        for observer in self._observers:
            observer.update(state)

    def feed(self, food):
        state = f"{self.name} est nourri avec {food}."
        self.notify_observers(state)
        self.satisfied = True
        

