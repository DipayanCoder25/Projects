         
class dog:
    def __init__(self,breed_name,age):
        self.breed_name=breed_name
        self.age=age
    def disply(self):
        print("The breed name of dog is ",self.breed_name)
        print("The age of the dog is ",self.age) 
        
mix1=dog("Mixed",13)
mix1.disply()   
mix2=dog("Mixed",14)
mix2.disply()