class Dog:
    
    species = "Husky,Golden Retriever,German Sheapeard"
    
    
    def __init__(self, name, breed):
        self.name = name    
        self.breed = breed  

  
    def displaydetails(self):
        print("Name: {self.name}")
        print("Breed: {self.breed}")
        print("Species: {Dog.species}") 


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Bella", "German Shepherd")


print("Dog 1 Details:")
dog1.displaydetails()

print("\nDog 2 Details:")
dog2.displaydetails()
