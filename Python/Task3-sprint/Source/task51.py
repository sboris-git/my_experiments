class American:

    @staticmethod
    def printNationality(nationality):
        print(nationality)

class NewYorker(American):
    pass

obj = NewYorker()
NewYorker().printNationality('Ukrainian')
