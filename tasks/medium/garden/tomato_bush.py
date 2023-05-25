from belhard_8_tasks.tasks.medium.garden.tomato import Tomato


class TomatoBush:
    """Класс куст с помидорами"""

    def __init__(self, *args) -> None:
        self.tomatoes_list = list(args)

    def grow_all(self) -> None:
        """переводит все объекты из списка томатов на следующий этап созревания"""

        for tomato in self.tomatoes_list:
            tomato.grow()

    def all_are_ripe(self) -> bool:
        """проверка всех томатов на спелость"""

        return all([tomato.is_ripe() for tomato in self.tomatoes_list])

    def give_away_all(self) -> list:
        """список томатов которые будут собраны на кустах"""

        tomatoes_list = self.tomatoes_list.copy()
        self.tomatoes_list.clear()

        return tomatoes_list


