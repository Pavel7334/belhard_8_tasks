"""
Описать абстрактный класс Transport:

- атрибут brand - фирма, выпустившая транспорт (тип - str)
- атрибут model - модель (тип - str)
- атрибут issue_year - год выпуска (тип - int)
- атрибут color - цвет (тип - str)
- атрибут mileage - пробег (тип - int)
- магический метод __init__, который принимает brand, model, issue_year и color,
  а mileage устанавливает значение 0
- абстрактный метод move, который принимает num_km - количество километров,
  которое должен пройти транспорт, проверяет, чтобы num_km было больше 0 и
  увеличивает mileage на значение num_km. Если num_km меньше 0, то бросить
  исключение ValueError("Расстояние должно быть положительным числом")

Описать класс Car, который наследуется от Transport:

- атрибут engine_type - тип двигателя (тип str)
- магический метод __init__, который принимает brand, model, issue_year и color
  и engine_type
- переопределить метод move. Внутри метода вызвать родительский метод, а потом
  вернуть строку "{brand} {model} ({color} - {issue_year}) проехала {km}
  километров"

Описать класс Airplane, который наследуется от Transport:

- атрибут lifting_capacity - грузоподъемность (тип - int)
- магический метод __init__, который принимает brand, model, issue_year и color
  и lifting_capacity
- переопределить метод move. Внутри метода вызвать родительский метод, а потом
  вернуть строку "{brand} {model} ({color} - {issue_year}) пролетел {km}
  километров"
"""
from abc import abstractmethod, ABC


class Transport(ABC):

    @abstractmethod
    def __init__(self, brand: str, model: str, issue_year: int, color: str) -> None:
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.mileage = 0

    @abstractmethod
    def move(self, num_km: int) -> None:
        if num_km > 0:
            self.mileage += num_km
        else:
            raise ValueError("Расстояние должно быть положительным числом")


class Car(Transport):

    def __init__(self,  brand: str, model: str, issue_year: int, color: str, engine_type: str) -> None:
        super().__init__(brand, model, issue_year, color)
        self.engine_type = engine_type

    def move(self, num_km: int) -> str:
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) проехала {num_km} километров"


class Airplane(Transport):

    def __init__(self, brand: str, model: str, issue_year: int, color: str, lifting_capacity: int) -> None:
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self, num_km) -> str:
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) пролетел {num_km} километров"

