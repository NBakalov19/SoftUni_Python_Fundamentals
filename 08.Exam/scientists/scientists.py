from abc import ABC, abstractmethod


class Species:
    def __init__(self, name: str, type_spice: str):
        self.name = name
        self.type_spice = type_spice

    def __str__(self):
        return f'- {self.name} ({self.type_spice})'


class Element:
    def __init__(self, name: str, type_element: str):
        self.name = name
        self.type_element = type_element

    def __str__(self):
        return f'- {self.name} ({self.type_element})'


class Scientist(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def __str__(self):
        return ''


class Biologist(Scientist):
    def __init__(self, name, age):
        Scientist.__init__(self, name, age)
        self.researched_species = []

    def add_species(self, spice):
        if isinstance(spice, Species):
            self.researched_species.append(spice)
        else:
            raise Exception('This is not a species')

    def __str__(self):
        species = '\n'.join(map(str, sorted(self.researched_species, key=lambda e: e.name)))

        if len(species) > 0:
            return f'{self.name} is {self.age} years old Biologist with {len(self.researched_species)}' + \
                   f' researched species:\n{species}'
        else:
            return f'{self.name} is {self.age} years old Biologist with {len(self.researched_species)}' + \
                   f' researched species:'


class Chemist(Scientist):
    def __init__(self, name, age):
        Scientist.__init__(self, name, age)
        self.researched_elements = []

    def add_element(self, element):
        if isinstance(element, Element):
            self.researched_elements.append(element)
        else:
            raise Exception('This is not a element')

    def __str__(self):
        elements = '\n'.join(map(str, sorted(self.researched_elements, key=lambda e: e.name)))

        if len(elements) > 0:
            return f'{self.name} is {self.age} years old Chemist with {len(self.researched_elements)}' + \
                   f' researched elements:\n{elements}'
        else:
            return f'{self.name} is {self.age} years old Chemist with {len(self.researched_elements)}' + \
                   f' researched elements:'


def is_scientist_or_element_exist(name: str, collection: list):
    return next(filter(lambda s: s.name == name, collection), None)


if __name__ == '__main__':
    scientist_count = int(input())

    scientist_list = []
    elements_list = []

    for scientist in range(scientist_count):
        line = input()

        curr_type = eval(line)
        if isinstance(curr_type, Biologist) or isinstance(curr_type, Chemist):
            scientist_list.append(curr_type)
        else:
            elements_list.append(curr_type)

    commands_count = int(input())

    for cmd in range(commands_count):
        scientist_name, scientist_method, item = input().split('-')

        scientist: Scientist = is_scientist_or_element_exist(scientist_name, scientist_list)
        item = is_scientist_or_element_exist(item, elements_list)

        if scientist is not None:
            if item is not None:
                if hasattr(scientist, scientist_method):
                    if isinstance(scientist, Biologist):
                        try:
                            scientist.add_species(item)
                        except Exception as ex:
                            print(ex)
                    elif isinstance(scientist, Chemist):
                        try:
                            scientist.add_element(item)
                        except Exception as ex:
                            print(ex)
                else:
                    print(f'Scientist has no such method')
            else:
                print('No such element or species')
        else:
            print('No such scientist')

    for scientist in sorted(scientist_list, key=lambda s: (-s.age, s.name)):
        print(scientist)
