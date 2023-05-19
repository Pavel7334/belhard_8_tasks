

class Gardener:
    """Класс садовник"""

    def __init__(self, name: str, plant: str) -> None:
        self.name = name
        self._plant = plant

    def work(self):
        """работать садовнику для роста кустов"""

        self._plant.grow_all()

    def harvest(self) -> None:
        """проверка, все ли плоды соспели"""

        if self._plant.all_are_ripe():
            print('Урожай собран!')
            self._plant.give_away_all()

        else:
            print('Томаты ещё не дозрели')

