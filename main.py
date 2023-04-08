class Cat:
    def __init__(self, name):
        self.name = name

    def play(self, person):
        print('Im playning with', person.name)
        person.isHappy = True

class Person:
    isHappy = False

    def __init__(self,name, age):
        self.name = name
        self.age = age


my_cat = Cat("Murzik")
me = Person('saha', 22)
friend = Person('vany', 20)

my_cat.play(me)
my_cat.play(friend)
