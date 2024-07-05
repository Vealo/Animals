class Animals:
    description: str = "It's a life"

    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age

    def get_description(self):
        print("Описание класса:", str(self.__class__.description))

    def move(self, environment='earth'):
        if environment == 'earth':
            return self.run()
        else:
            print(f'{self.name} is moving')

    def run(self):
        print(f"{self.name} is moving")


class Birds(Animals):
    description: str = "Птицы"

    def move(self, environment='air'):
        if environment == 'air':
            return self.flying()
        elif environment == 'earth':
            return self.run()

    def flying(self):
        print(f"{self.name} is fly")

    def run(self):
        print(f"{self.name} is jump")


class Mammals(Animals):
    description: str = "Млекопитающие"

    def move(self, environment='air'):
        if environment == 'air':
            return self.jump()
        elif environment == 'earth':
            return self.run()

    def jump(self, environment='air'):
        print(f"{self.name} is jump")


class Griffin(Birds, Mammals):
    description: str = "Это мифическое животное наполовину орел наполовину лев"


lst = [Animals('Cat', 11), Birds('Eagle', 1), Mammals('Gazel', 2), Griffin('Вася', 53)]

for animal in lst:
    print(f'{animal.__class__} зовут: {animal.name} возраста: {animal.age}')
    print(animal.__class__.mro())
    print('-' * 10, end='\n\n')
