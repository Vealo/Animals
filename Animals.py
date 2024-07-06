#Mixin: Классы миксины Run, Jump, Fly
class Run:
    "Класс миксин: бег - вариант передвиженрия по земле"
    def run(self):
        print(f"{self.name} is moving")

class Jump:
    "Класс миксин: прыжок - вариан передвиженрия в воздухе для сухопутных"
    def jump(self):
        print(f"{self.name} is jump")

class Fly:
    "Класс миксин: прыжок - вариан передвиженрия в воздухе для летающих животных"
    def fly(self):
        print(f"{self.name} is fly")

class Animals:
    'Базовый класс от него наследуется все классы животных'
    description: str = "It's a life"

    def __init__(self, name, age, legs=4, color='Black', sex='men') -> None:
        self.name: str = name
        self.age: int = age
        self.legs: int = legs
        self.color: str = color
        self.sex: str = sex

    def get_description(self):
        print("Описание класса:", str(self.__class__.description))

    def move(self, environment='earth'):
        print(f'{self.name} is moving')

    def __str__(self):
        return f'Животное по имени {self.name}'

    def __repr__(self):
        return f'Animal({self.name, self.age})'


class Birds(Animals, Fly):
    description: str = "Птицы"

    def move(self, environment='air'):
        if environment == 'air':
            return self.flying()
        elif environment == 'earth':
            return self.run()

    def flying(self):
        print(f"{self.name} is fly")

    def __str__(self):
        return f'Птица по имени {self.name}'

    def __repr__(self):
        return f'Birds({self.name, self.age})'


class Mammals(Animals, Run, Jump):
    description: str = "Млекопитающие"

    def move(self, environment='air'):
        if environment == 'air':
            return self.jump()
        elif environment == 'earth':
            return self.run()

    def __str__(self):
        return f'Млекопетающие по имени {self.name}'

    def __repr__(self):
        return f'Mammals({self.name, self.age})'

class Griffin(Birds, Mammals):
    description: str = "Это мифическое животное наполовину орел наполовину лев"

    def __str__(self):
        return f'Грифон {self.name}'

    def __repr__(self):
        return f'Griffin({self.name, self.age})'


lst = [Animals('Cat', 11), Birds('Eagle', 1), Mammals('Gazel', 2), Griffin('Вася', 53)]

for animal in lst:
    print(animal)
    print(repr(animal), end='\n\n')
