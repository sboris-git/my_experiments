from datetime import date

# random Person
class Person:
    def __init__( self, name, age ):
        self.name = name
        self.age = age


    @staticmethod
    def fromBirthYear( name, birthYear ):
        return Person(name, date.today().year - birthYear) # but this is equivalent to @classmethod
        # www.programiz.com/python-programming/methods/built-in/classmethod
        # The paragraph just before chapter 2 or the Example 3
    '''
        @classmethod
        def fromBirthYear( cls, name, birthYear ):
            return cls(name, date.today().year - birthYear)

        def display( self ):
            print(self.name + "'s age is: " + str(self.age))
    '''

    def display( self ):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John', 1985)
person1.display()