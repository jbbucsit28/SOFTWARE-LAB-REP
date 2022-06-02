
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'Person(' + self.name + ',' + str(self.age) + ')'
        return rep


# Let's make a Person object and print the results of repr()

person = Person("John", 21)
print(repr(person))