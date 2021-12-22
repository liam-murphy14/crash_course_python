class Restaurant:
    """ simulates a restaurant, badly """

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    

    def describe(self):
        print(f"We are {self.name} and we sell {self.cuisine} food")
    

    def open_restaurant(self):
        print("we be open now")

my_rest = Restaurant("incorp", "American")
my_rest.describe()

class  IceCreamStand(Restaurant):
    """ a more specific restaurant """

    def __init__(self, name):
        super().__init__(name, "dessert")
        self.flavors = ["vanilla", "chocolate", "superman"]


    def get_flavs(self):
        print(self.flavors)

tates = IceCreamStand("tates")
tates.describe()
tates.get_flavs()