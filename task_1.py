from random import randint
class  Animal:
    def __init__(self, type_animal, name, weight):
        self.type_animal = type_animal
        self.name = name
        self.weight = weight
    def feed(self):
        self.weight += 1
        print(f'{self.type_animal} {self.name} накормелн(а). {self.name} набрала в весе и теперь весит {self.weight} кг')
    def individual_approach(self):
        if self.type_animal == 'Гусь' or self.type_animal == 'Курица' or self.type_animal == 'Утка':
            print(f'{self.type_animal} {self.name} снесла яйца! Вы собрали {randint(1, 10)} яйца')
        elif self.type_animal == 'Корова' or self.type_animal == 'Овца' or self.type_animal == 'Коза':
            print(f'Вам удалось выдоить молоко. {self.type_animal} {self.name} доволна!')
    def comb(self):
        if self.type_animal == 'Корова' or self.type_animal == 'Овца' or self.type_animal == 'Коза':
            print(f'Вы вычесали животное. {self.type_animal} {self.name} теперь красивая!')

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



type_animal_dict = {'Гусь': [2, ['Серый', 'Белый'], [5, 7]], 'Корова' : [1, ['Манька'], [100]], 'Овца' : [2, ['Барашек', 'Кудрявый'], [46, 54]], 'Курица' : [2, ['Ко-Ко', 'Кукареку'], [3, 5]], 'Коза' : [2, ['Рога', 'Копыта'], [7, 10]], 'Утка' : [1, ['Кряква'], [6]]}

animals = []

for animal in list(type_animal_dict.items()):
    for i in range(int(animal[1][0])):
        enter_animal = Animal(animal[0], animal[1][1][i], animal[1][2][i])
        animals.append(enter_animal)

# Для проверки записи всех животных в список выведем проверку наличия имен
# for index, animal in enumerate(animals):
#     print(index, animal.name)

# Для удобства обращения (так как при обращении просто к элементу списка не понятно, какое это животное):
goose_1, goose_2, cow, sheep_1, sheep_2, chiken_1, chiken_2, goat_1, goat_2, duck = animals

sum_wight_animals(animals)
max_wieght(animals)
