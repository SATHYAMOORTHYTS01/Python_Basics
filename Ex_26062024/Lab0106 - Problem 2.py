class Dog:
    # Attributes
    name = None # None - Default value
    breed = None
    age = None
    color = None

    # constructor - A speical methods

    def __init__(self,name,id,bread,color): # Constructor __ - private method
        self.name = name  #### self - means current object
        self.id = id
        self.breed = bread
        self.color = color

    # Behaviour (Methods)
    def sleep(self):
        print("Who is  Sleeping" + " " +self.name + " " + self.id + " " +self.breed + " " + self.color)


dog1 =  Dog("Tommy", "1" , "labrador" , "white") # these are objects1 created
dog2 =  Dog("Mow", "2" , "labrador" , "black") # these are objects2 created
dog3 =  Dog("Buddy", "3" , "labrador" , "gold")
dog4 =  Dog("Whiskey", "4" , "labrador", "brown")

print(f"Dog1: {dog1.name} {dog1.id} {dog1.breed} {dog1.color}")
print(f"Dog2: {dog2.name} {dog2.id} {dog2.breed} {dog2.color}")
print(f"Dog3: {dog3.name} {dog3.id} {dog3.breed} {dog3.color}")
print(f"Dog4: {dog4.name} {dog4.id} {dog4.breed} {dog4.color}")


dog1.sleep()
dog2.sleep()
dog3.sleep()
dog4.sleep()





