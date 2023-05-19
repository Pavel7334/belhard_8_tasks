from belhard_8_tasks.tasks.medium.garden.gardener import Gardener
from belhard_8_tasks.tasks.medium.garden.tomato_bush import TomatoBush

# Создание объектов класса TomatoBush
bush = TomatoBush(5)
bush1 = TomatoBush(6)

# Создание объектов класса Gardener
gardener = Gardener('John', bush)

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


if __name__ == '__main__':
    pass
