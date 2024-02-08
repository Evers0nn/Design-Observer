class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.notify(message)

class BattleSubject(Subject):
    def __init__(self):
        super().__init__()
        self.last_battle_result = None

    def finish_battle(self, result):
        self.last_battle_result = result
        self.notify_observers(result)

    def get_last_battle_result(self):
        return self.last_battle_result

class Observer:
    def notify(self, message):
        pass

class PlayerObserver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f"Jogador {self.name}: {message}")

battle_subject = BattleSubject()
