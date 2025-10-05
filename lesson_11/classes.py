from abc import abstractmethod

# Если класс имеет абстрактный метод, то автоматически становится абстрактным классом
class Group:
    pupils = True
    school_name = 42
    director = 'Marivanna'

    def __init__(self, title, pupils_count, group_leader):
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader

    def study(self):
        print('Sit down and read')

    @abstractmethod  # декоратор обозначающий абстрактный метод
    def move(self):
        pass


class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = 'left'

    def move(self):
        print('Run fast')

    def __init__(self, title, pupils_count, group_leader, class_room):
        super().__init__(title,pupils_count, group_leader)
        self.class_room = class_room

class HighGroup(Group):
    max_age = 18
    min_age = 14
    def move(self):
        print('Run slow')

class MediumGroup(Group):
    max_age = 15
    min_age = 10

# объект класса = объект типа = представитель класса = экземпляр класса

first_a = PrimaryGroup('1a', 18, 'MF', 5)
first_b = PrimaryGroup('1b', 20, 'TD', 8)
eleven_a = HighGroup('11a', 22, 'AR')
six_a = MediumGroup('6a', 25, 'RI')

print(first_a.pupils_count)
print(first_a.class_room)
print(first_b.class_room)
print(first_a.title)
print(first_b.title)
print(first_a.pupils)
first_a.study()
eleven_a.study()
first_a.move()
eleven_a.move()
six_a.move()