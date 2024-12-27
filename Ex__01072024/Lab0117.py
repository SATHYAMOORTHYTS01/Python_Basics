# Single Inheritance

#Parent Class
class Grandparent:

    key = "@1234221"

    def grandparent_method(self):
        return "Grandparent method called"

#Child class, Sub class
class Father(Grandparent):    # Grandparent is a inheritance
    def parent_method(self):
        return " Parents's method called"


parent = Father()
parent.parent_method()
parent.grandparent_method() # how parent is able to call the grandparent? because of Inheritacne
print(parent.key)