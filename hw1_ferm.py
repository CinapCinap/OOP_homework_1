class Animal:
    voice = ''
    type = ''
    ferm_list = []
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.ferm_list.append(self)
    def eat(self):
        print(f'{self.type} {self.name} - покормили, {self.voice}')
    def count_total_weight(cls):
        total_weight = 0
        for animal in Animal.ferm_list:
            total_weight += animal.weight
        print(f'Общий вес всех животных - {total_weight} кг')
    def find_heaviest(cls):
        max_weight = 0
        for animal in Animal.ferm_list:
            if animal.weight > max_weight:
                max_weight = animal.weight
                heaviest_animal = animal
        print(f'Самое тяжелое животное на ферме - {heaviest_animal.type} {heaviest_animal.name}, весит {heaviest_animal.weight} кг')
class Bird(Animal):        
    def collect_eggs(self):
        print(f'{self.type} {self.name} - собрали яйца, {self.voice}')
class Goose(Bird):
    voice = 'га-га-га'
    type = 'Гусь'
class Chicken(Bird):
    voice = 'кудах-кудах'
    type = 'Курица'
class Duck(Bird):
    voice = 'кря-кря-кря'
    type = 'Утка'
class Milky_mammal(Animal):
    def milk(self):
        print(f'{self.type} {self.name} - подоили, {self.voice}')
class Cow(Milky_mammal):
    voice = 'мууу'
    type = 'Корова'        
class Sheep(Animal):
    voice = 'беее'
    type = 'Овца'
    def shave(self):
        print(f'{self.type} {self.name} - обстригли, {self.voice}')
class Goat(Milky_mammal):
    voice = 'меее'
    type = 'Коза'
#задание 1
seriy = Goose('Серый', 3)
beliy = Goose('Белый', 2)
manka = Cow('Манька', 10)
barash = Sheep('Барашек', 5)
kudr = Sheep('Кудрявый', 6)
koko = Chicken('Ко-ко', 1.3)
kuka = Chicken('Кукареку', 1.7)
roga = Goat('Рога', 7)
kopita = Goat('Копыта', 9)
kryak = Duck('Кряква', 1)
seriy.eat()
beliy.eat()
manka.eat()
barash.eat()
kudr.eat()
koko.eat()
kuka.eat()
roga.eat()
kopita.eat()
kryak.eat()
manka.milk()
roga.milk()
kopita.milk()
barash.shave()
kudr.shave()
seriy.collect_eggs()
beliy.collect_eggs()
koko.collect_eggs()
kuka.collect_eggs()
kryak.collect_eggs()
#задание 2
Animal.count_total_weight(Animal)
Animal.find_heaviest(Animal)
