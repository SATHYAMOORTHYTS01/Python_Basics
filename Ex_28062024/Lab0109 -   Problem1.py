class Car:

    name = None
    model = None
    year = None

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def start_engine(self):
        print("Starting the car with name" + self.name)
        print("Starting the car with model" + self.model)
        print("Starting the car with year" + str(self.year))
# This is end of the class


lambo = Car("Lambor", "Aventador", 2020)
lambo.start_engine()

xuv = Car("XUV", "500", 2019)
xuv.start_engine()