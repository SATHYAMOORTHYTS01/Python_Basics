class VWOLoginPage:

    email = None
    password = None


    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        #used two conditions here
        if self.email == "amit@gmail.com"  and  self.password == "Pass23":
            print("Login allowed")
        else:
            print("Login not allowed")
# This is end of the class

#object creation
email = input("Enter your email: \n")
password = input("Enter your password: \n")

amit = VWOLoginPage("amit@gmail.com", "pass23")
amit.login_confirm()

sathya = VWOLoginPage("sathya@gmail.com", "123")
sathya.login_confirm()