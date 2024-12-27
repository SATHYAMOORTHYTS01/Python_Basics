class VWOLogin:
    """
    This class represents a login page for a vehicle warranty organization (VWO) website.
    It takes two arguments: email and password, and provides a method to confirm the login.
    """

    def __init__(self,email,password,name):
        self.__email = email
        self.__password = password
        self.name = "VWO"
        self.__name = "abc"

    def login_confirm(self):
        if self.__email == "aaa@gmail.com" and self.__password == "admin@123":
            print("Login successful")
        else:
            print("Login failed")
#This is end of the class

page1 = VWOLogin("aaa@gmail.com", "admin@123", "VWO")  # object creation
page1.login_confirm()
print(page1.name)