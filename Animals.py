#Mixin: Классы миксины Run, Jump, Fly
class Run:
    "Класс миксин: бег - вариант передвиженрия по земле"
    def run(self) -> str:
        print(f"{self.name} is moving")

class Jump:
    "Класс миксин: прыжок - вариан передвиженрия в воздухе для сухопутных"
    def jump(self) -> str:
        print(f"{self.name} is jump")

class Fly:
    "Класс миксин: прыжок - вариан передвиженрия в воздухе для летающих животных"
    def fly(self) -> str:
        print(f"{self.name} is fly")

class Animals:
    'Базовый класс от него наследуется все классы животных'
    description: str = "It's a life"

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.legs: int = 4
        self.color: str = 'Black'
        self.sex: str = 'men'

    def get_description(self) -> str:
        print("Описание класса:", str(self.__class__.description))

    def move(self, environment: str='earth') -> str:
        print(f'{self.name} is moving')

    def __str__(self) -> str:
        return f'Животное по имени {self.name}'

    def __repr__(self) -> str:
        return f'Animal({self.name, self.age})'


class Birds(Animals, Fly):
    description: str = "Птицы"

    def __init__(self, name, age):
        Animals.__init__(self, name, age)
        self.legs: int = 2

    def move(self, environment: str = 'air') -> str:
        if environment == 'air':
            return self.flying()
        elif environment == 'earth':
            return self.run()

    def flying(self) -> str:
        print(f"{self.name} is fly")

    def __str__(self) -> str:
        return f'Птица по имени {self.name}'

    def __repr__(self) ->str:
        return f'Birds({self.name, self.age})'


class Mammals(Animals, Run, Jump):
    description: str = "Млекопитающие"

    def move(self, environment='air') -> str:
        if environment == 'air':
            return self.jump()
        elif environment == 'earth':
            return self.run()

    def __str__(self) -> str:
        return f'Млекопетающие по имени {self.name}'

    def __repr__(self) -> str:
        return f'Mammals({self.name, self.age})'

class Griffin(Birds, Mammals):
    description: str = "Это мифическое животное наполовину орел наполовину лев"

    def __init__(self, name: str, age: str) -> None:
        Birds.__init__(self, name, age)
        self.legs: int = 4
    def __str__(self) -> str:
        return f'Грифон {self.name}'

    def __repr__(self) -> str:
        return f'Griffin({self.name, self.age})'

#New class Eagle, Cat, White_Griffin

class Eagle(Birds):

    description = 'Гордый крылатый хишник с мошным клювом и отличным зрением - Орел'

    def __init__(self, name, age) -> None:
        Birds.__init__(self, name, age)
        self.color = 'Broun'
    def __str__(self)  -> str:
        return f'Орел по имени {self.name}'

    def __repr__(self)  -> str:
        return f'Eagle({self.name, self.age})'

class Cat(Mammals):

    description = 'Чудный мелкий пушистик спасающтий людей от грызунов - Кот'

    def __str__(self)   -> str:
        return f'Кот по имени {self.name}'

    def __repr__(self)  -> str:
        return f'Cat({self.name, self.age})'

class White_Griffin(Griffin):

    description = 'Самый крупный представитель этих легендарных мифических животных - Белый Гриффон'

    def __init__(self, name, age)  -> None:
        Birds.__init__(self, name, age)
        self.legs: int = 4
        self.color: str = 'White'

    def __str__(self)  -> str:
        return f'Белый гриффон по имени {self.name}'

    def __repr__(self) -> str:
        return f'White_Griffin({self.name, self.age})'


lst = [
       Animals('Cat', 11),
       Birds('Орел', 2),
       Mammals('Gazel', 2),
       Griffin('Вася', 53),
       Cat('Пушистик', 2),
       Eagle('Птер', 5),
       White_Griffin('Лорд', 14)
       ]

for animal in lst:
    print(animal)
    print(repr(animal), end='\n\n')
