class City:
    city = "City"

    def __init__(self, city = None):
        self.city = city


usa = City("NY")
print("{} is {}".format(City.city, usa.city))

canada = City()
canada.city = "Toronto"

print("{} is {}".format(City.city, canada.city))