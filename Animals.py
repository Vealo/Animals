#Mixin: Классы миксины Run, Jump, Fly
class Run:
    def run(self):
        print(f"{self.name} is moving")

class Jump:
    def jump(self):
        print(f"{self.name} is jump")

class Fly:
    def fly(self):
        print(f"{self.name} is fly")

class Animals:
    description: str = "It's a life"

    def __init__(self, name, age, legs=4, color='Black', sex='men'):
        self.name: str = name
        self.age: int = age
        self.legs: int = legs
        self.color: str = color
        self.sex: str = sex

    def get_description(self):
        print("Описание класса:", str(self.__class__.description))

    def move(self, environment='earth'):
        print(f'{self.name} is moving')


class Birds(Animals, Fly):
    description: str = "Птицы"

    def move(self, environment='air'):
        if environment == 'air':
            return self.flying()
        elif environment == 'earth':
            return self.run()

    def flying(self):
        print(f"{self.name} is fly")


class Mammals(Animals, Run, Jump):
    description: str = "Млекопитающие"

    def move(self, environment='air'):
        if environment == 'air':
            return self.jump()
        elif environment == 'earth':
            return self.run()


class Griffin(Birds, Mammals):
    description: str = "Это мифическое животное наполовину орел наполовину лев"


lst = [Animals('Cat', 11), Birds('Eagle', 1), Mammals('Gazel', 2), Griffin('Вася', 53)]

for animal in lst:
    animal.move()
