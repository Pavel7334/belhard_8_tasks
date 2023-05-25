from belhard_8_tasks.tasks.medium.garden.gardener import Gardener
from belhard_8_tasks.tasks.medium.garden.tomato import Tomato
from belhard_8_tasks.tasks.medium.garden.tomato_bush import TomatoBush

# Создание объектов класса TomatoBush
tomato = Tomato(2)
tomato1 = Tomato(1)
tomato2 = Tomato(3)
tomato3 = Tomato(2)
tomato4 = Tomato(1)
tomato5 = Tomato(3)
bush = TomatoBush(tomato, tomato2, tomato3)
bush1 = TomatoBush(tomato1, tomato4, tomato5)

# print(len(bush1.tomatoes_list))


# Создание объектов класса Gardener
gardener = Gardener('John', bush, bush1)


# Уход за кустом с помидорами
gardener.work()
gardener.work()
gardener.work()


# Сбор урожая
gardener.harvest()

# Продолжение ухода за кустом, пока томаты не дозреют
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
# Сбор урожая после дозревания всех томатов
gardener.work()
gardener.harvest()
gardener.harvest()
print(len(gardener.harvest()))

if __name__ == '__main__':
    pass
