

class Gardener:
    """Класс садовник"""

    def __init__(self, name: str, *args) -> None:
        self.name = name
        self._plants = args

    def work(self) -> None:
        """работать садовнику для роста кустов"""

        for plant in self._plants:
            plant.grow_all()

    def harvest(self) -> list:
        """проверка, все ли плоды соспели"""

        result_list = []
        if all([plant.all_are_ripe() for plant in self._plants]):
            for plant in self._plants:
                for tomato in plant.tomatoes_list:
                    result_list.append(tomato)
            return result_list
        else:
            print("Томаты не созрели")



