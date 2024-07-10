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

#Basic class
class Animals:
    'Базовый класс от него наследуется все классы животных'
    description: str = "It's a life"

    def __init__(self, name: str, age: int) -> None:
        self._name: str = name
        self.age: int = age
        self.legs: int = 4
        self._color: str = 'Black'
        self.sex: str = 'men'
        self._class_name: str = 'Животное'
        self._class_type: str = 'Animal'

    #Block get / set
    #Function property

    def get_name(self):
        return self._name

    def set_name(self, name='Black'):
        print(name)
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    name = property(get_name, set_name)

    #Decoration property

    @property
    def color(self):                                     # геттер свойства color
        return self._color

    @color.setter
    def color(self, color):                               # сеттер свойства color
        if isinstance(color, str) and color.isalpha():
            self._color = color
        else:
            raise ValueError('Некорректное имя')

    @color.deleter
    def color(self):                                     # делитер свойства color
        del self._color

    @classmethod
    def get_description(cls) -> str:
        print("Описание класса:", str(cls.description))

    def move(self, environment: str='earth') -> str:
        print(f'{self.name} is moving')

    def __str__(self) -> str:
        return f'{self._class_name} по имени: {self.name}'

    def __repr__(self) -> str:
        return f'{self._class_type}({self.name, self.age})'


class Birds(Animals, Fly, Jump):
    description: str = "Птицы"

    def __init__(self, name, age):
        Animals.__init__(self, name, age)
        self.legs: int = 2
        self._class_name: str = 'Птица'
        self._class_type: str = 'Birds'

    def move(self, environment: str = 'air') -> str:
        if environment == 'air':
            return self.fly()
        elif environment == 'earth':
            return self.jump()

class Mammals(Animals, Run, Jump):
    description: str = "Млекопитающие"

    def __init__(self, name, age):
        Animals.__init__(self, name, age)
        self._class_name: str = 'Млекопитающие'
        self._class_type: str = 'Mammals'
    def move(self, environment='air') -> str:
        if environment == 'air':
            return self.jump()
        elif environment == 'earth':
            return self.run()

class Griffin(Birds, Mammals):
    description: str = "Это мифическое животное наполовину орел наполовину лев"

    def __init__(self, name: str, age: str) -> None:
        Birds.__init__(self, name, age)
        self.legs: int = 4
        self._class_name: str = 'Гриффон'
        self._class_type: str = 'Griffin'


#New class Eagle, Cat, White_Griffin
#Extended class
class Eagle(Birds):

    description = 'Гордый крылатый хишник с мошным клювом и отличным зрением - Орел'

    def __init__(self, name, age) -> None:
        Birds.__init__(self, name, age)
        self.color = 'Broun'
        self._class_name: str = 'Орел'
        self._class_type: str = 'Eagle'

class Cat(Mammals):

    description = 'Чудный мелкий пушистик спасающтий людей от грызунов - Кот'

    def __init__(self, name, age) -> None:
        Birds.__init__(self, name, age)
        self._class_name: str = 'Кот'
        self._class_type: str = 'Cat'

class White_Griffin(Griffin):

    description = 'Самый крупный представитель этих легендарных мифических животных - Белый Гриффон'

    def __init__(self, name, age)  -> None:
        Birds.__init__(self, name, age)
        self.legs: int = 4
        self.color: str = 'White'
        self._class_name: str = 'Белый Гриффон'
        self._class_type: str = 'White_Griffin'



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
    animal.get_description()
    print(repr(animal))
    animal.move()
    animal.move(environment='earth')
    animal.move(environment='air')
    print('-' * 15)
    __import__('time').sleep(1)


