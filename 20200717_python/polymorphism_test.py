# abstract method를 가진 부모 클래스 선언
class Animal(object):
    def __init__(self, name):
        self.name = name

    # abstract method
    def talk(self):
        raise NotImplementedError('자식 클래스에서 반드시 구현해야 함')


class Cat(Animal):
    def talk(self):
        return 'Mew'


class Dog(Animal):
    def talk(self):
        return 'Moof'

    def pet(self):
        return "I'm a Pet"


my_ani = Cat('동물')
print(my_ani.name)
# my_ani.talk()

animals = [Cat('고양이'), Dog('강아지'), Dog('멍멍이')]
for ani in animals:
    print(ani.talk())
    # print(ani.pet())
