class Account:

    def __init__(self, AccountNumber, AccountPassword):
        self.AccountNumber = AccountNumber
        self.AccountPassword = AccountPassword

    def AccountLogin(self):
        if self.AccountNumber == input("Enter your Account Number: \n") and self.AccountPassword == input("Enter your Password: \n"):
            print("Login successful")
        else:
            print("Login failed")
            print("Incorrect Account Number or Password")


sathya = Account("1234567890", "Sathya@123")
sathya.AccountLogin()
print("\n")
amit = Account("0987654321", "Amit@123")
amit.AccountLogin()

