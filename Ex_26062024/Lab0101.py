# Class and Objects
#  Class is a blueprint for creating objects
class MyClass:
    x = 5  # Class attribute
    def __init__(self):  # Constructor
        self.y = 10  # Instance attribute
        print("Hello World")  # Instance method
        print(self.x)  # Accessing class attribute
        print(self.y)  # Accessing instance attribute
        self.y = 20  # Modifying instance attribute
        print(self.y)  # Accessing modified instance attribute
        del self.y  # Deleting instance attribute
        print(self.y)  # Accessing deleted instance attribute (will raise an error)
        print(self.x)  # Accessing class attribute
        print(MyClass.x)  # Accessing class attribute using class name
        print(self.__class__.x)  # Accessing class attribute using __class__ attribute
        print(MyClass.__name__)  # Accessing class name
        print(self.__module__)  # Accessing module name
        print(self.__dict__)  # Accessing instance attributes as a dictionary
        print(self.__class__.__dict__)  # Accessing class attributes as a dictionary
        print(MyClass.__dict__)  # Accessing class attributes as a dictionary using class name
        print(MyClass.__bases__)  # Accessing base classes
        print(MyClass.__doc__)  # Accessing class documentation string
        print(MyClass.__init__.__doc__)  # Accessing method documentation string
        print(MyClass.__init__.__name__)  # Accessing method name
        print(MyClass.__init__.__module__)  # Accessing module name
        print(MyClass.__init__.__defaults__)  # Accessing default argument values
        print(MyClass.__init__.__code__)  # Accessing method code object
        print(MyClass.__init__.__globals__)  # Accessing global namespace
        print(MyClass.__init__.__closure__)  # Accessing closure values
###