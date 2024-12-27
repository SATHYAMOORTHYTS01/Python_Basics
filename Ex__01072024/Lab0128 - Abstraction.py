
# Abstraction

# hiding the details adn showing the waht is required

class Animal:
    def __init__(self):
        self.name = "Animal"  # Public attribute

    @abstractmethod
    def make_sound(self):
        print("The animal makes a sound.")  # Public method
