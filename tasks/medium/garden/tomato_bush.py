from belhard_8_tasks.tasks.medium.garden.tomato import Tomato


class TomatoBush:
    """Класс куст с помидорами"""

    def __init__(self, num: int) -> None:
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self) -> None:
        """переводит все объекты из списка томатов на следующий этап созревания"""

        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self) -> bool:
        """проверка всех томатов на спелость"""

        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self) -> None:
        """список томатов которые будут собраны на кустах"""

        self.tomatoes = []


