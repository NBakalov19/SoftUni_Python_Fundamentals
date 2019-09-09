class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def produce_sound(self):
        return ''


class Dog(Animal):
    def __init__(self, name, age, number_of_legs: int):
        Animal.__init__(self, name, age)
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        return 'I\'m a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.'

    def __str__(self):
        return f'{__class__.__name__}: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}'


class Cat(Animal):
    def __init__(self, name, age, intelligence_quotient: int):
        Animal.__init__(self, name, age)
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        return 'I\'m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.'

    def __str__(self):
        return f'{__class__.__name__}: {self.name}, Age: {self.age}, IQ: {self.intelligence_quotient}'


class Snake(Animal):
    def __init__(self, name: str, age: int, cruelty_coefficient: int):
        Animal.__init__(self, name, age)
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        return 'I\'m a Sophistisnake, and I will now produce a sophisticated sound! Honey, I\'m home.'

    def __str__(self):
        return f'{__class__.__name__}: {self.name}, Age: {self.age}, Cruelty: {self.cruelty_coefficient}'


if __name__ == '__main__':

    data_list = input().split()

    animals_list = []

    while not data_list[0] == 'I\'m':
        animal_type = data_list[0]
        animal_name = data_list[1]

        if data_list[0] == 'talk':
            curr_animal = next(filter(lambda a: a.name == animal_name, animals_list))
            print(curr_animal.produce_sound())
        else:

            animal_age = int(data_list[2])
            specific_animal_item = int(data_list[3])

            animal = None

            if animal_type == 'Dog':
                animal = Dog(animal_name, animal_age, specific_animal_item)
            elif animal_type == 'Cat':
                animal = Cat(animal_name, animal_age, specific_animal_item)
            elif animal_type == 'Snake':
                animal = Snake(animal_name, animal_age, specific_animal_item)

            animals_list.append(animal)

        data_list = input().split()

    dogs_list = list(filter(lambda a: isinstance(a, Dog), animals_list))
    cats_list = list(filter(lambda a: isinstance(a, Cat), animals_list))
    snake_list = list(filter(lambda a: isinstance(a, Snake), animals_list))

    animals_list = dogs_list + cats_list + snake_list

    for animal in animals_list:
        print(animal)

