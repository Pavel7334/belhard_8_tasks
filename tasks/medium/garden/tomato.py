

class Tomato:
    """Класс помидор"""

    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}

    def __init__(self, index: int) -> None:
        self.index = index
        self._state = self.states['Отсутствует']

    def grow(self) -> str:
        """перевод на следующий этап созревания"""

        if self._state < 3:
            self._state += 1
        else:
            return f"Ваши томаты уже спелые"

    def is_ripe(self) -> bool:
        """проверка на созревание"""

        return True if self._state == 3 else False
