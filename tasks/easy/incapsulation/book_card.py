"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:

    def __init__(self, author: str, title: str, year: int) -> None:
        self.author = author
        self.title = title
        self.year = year

    def __eq__(self, other) -> bool:
        return self.__year == other.__year

    def __ne__(self, other) -> bool:
        return self.__year != other.__year

    def __lt__(self, other) -> bool:
        return self.__year < other.__year

    def __gt__(self, other) -> bool:
        return self.__year > other.__year

    def __le__(self, other) -> bool:
        return self.__year <= other.__year

    def __ge__(self, other) -> bool:
        return self.__year >= other.__year

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, x: str) -> None:
        if not isinstance(x, str):
            raise ValueError
        self.__author = x

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, x: str) -> None:
        if not isinstance(x, str):
            raise ValueError
        self.__title = x

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, x: int) -> None:
        if not isinstance(x, int):
            raise ValueError
        if x > CURRENT_YEAR:
            raise ValueError
        if x <= 0:
            raise ValueError
        self.__year = x

