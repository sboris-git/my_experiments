class Person:
    '''Question 95
    Define a class Person and its two child classes: Male and Female. All classes have
    a method "getGender" which can print "Male" for Male class and "Female" for Female class.'''

    def __init__(self):
        self.gender = 'Person'

    def getGender(self):
        print(self.gender)


class Male(Person):

    def __init__(self):
        self.gender = 'Male'


class Female(Person):

    def __init__(self):
        self.gender = 'Female'


person1 = Person()
person1.getGender()

person2 = Male()
person2.getGender()

person3 = Female()
person3.getGender()
