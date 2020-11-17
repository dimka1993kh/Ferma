from random import randint

class  Animal:
    def __init__(self, name, weight, type_animal):
        self.type_animal = type_animal
        self.name = name
        self.weight = weight
    def feed(self):
        self.weight += 1
        print(f'{self.type_animal} {self.name} накормелн(а). {self.name} набрала в весе и теперь весит {self.weight} кг')

class Bird(Animal):
    def __init__(self, name, weight, type_animal):
        super().__init__(name, weight, type_animal) 

    def collectEggs(self):
        print(f'{self.type_animal} {self.name} снесла яйца! Вы собрали {randint(1, 10)} яйца')

class Artiodactyl(Animal):
    def __init__(self, name, weight, type_animal):
        super().__init__(name, weight, type_animal) 

    def milk(self):
        print(f'Вам удалось выдоить молоко. {self.type_animal} {self.name} доволна!') 

    def comb(self):
        print(f'Вы вычесали животное. {self.type_animal} {self.name} теперь красивая!')  

class Goose(Bird):
    def __init__(self, name, weight, type_animal='Гусь'):
        super().__init__(name, weight, type_animal) 

class Cow(Artiodactyl):
    def __init__(self, name, weight, type_animal='Корова'):
        super().__init__(name, weight, type_animal) 

class Sheep(Artiodactyl):
    def __init__(self, name, weight, type_animal='Овца'):
        super().__init__(name, weight, type_animal) 

class Chicken(Bird):
    def __init__(self, name, weight, type_animal='Курица'):
        super().__init__(name, weight, type_animal) 

class Goat(Artiodactyl):
    def __init__(self, name, weight, type_animal='Коза'):
        super().__init__(name, weight, type_animal) 

class Duck(Bird):
    def __init__(self, name, weight, type_animal='Утка'):
        super().__init__(name, weight, type_animal) 


def sum_wight_animals(list_animals):
    sum_wight = 0
    for animal in list_animals:
        if not isinstance(animal, Animal):
            print('Не все "животные" являются животными')
        sum_wight += animal.weight
    return print(f'Вес всех животных составляет {sum_wight} кг')

def max_wieght(list_animals):
    weight_dict = {}
    for animal in list_animals:
        if not isinstance(animal, Animal):
            print('Не все "животные" являются животными')
        weight_dict.update({animal.name : animal.weight})
    return print(f'Имя самого тяжелого животного {sorted(list(weight_dict.items()), key=lambda x: x[1])[-1][0]}. Его вес {sorted(list(weight_dict.items()), key=lambda x: x[1])[-1][1]} кг')



goose_one = Goose('Серый', 5)
goose_two = Goose('Белый', 7)
cow = Cow('Манька', 100)
sheep_one = Sheep('Барашек', 15)
sheep_two = Sheep('Кудрявый', 20)
chicken_one = Chicken('Ко-Ко', 4)
chicken_two = Chicken('Кукареку', 5)
goat_one = Goat('Рога', 10)
goat_two = Goat('Копыта', 17)
duck = Duck('Кряква', 8)

animals = [goose_one, goose_two, cow, sheep_one, sheep_two, chicken_one, chicken_two, goat_one, goat_two, duck]

sum_wight_animals(animals)
max_wieght(animals)

# ПРОВЕРКА РАБОТОСПОСОБНОСТИ
print()
for animal in animals:
    animal.feed()
    if isinstance(animal, Bird):
        animal.collectEggs()
        print()
    elif isinstance(animal, Artiodactyl):
        animal.milk()
        animal.comb()
        print()

