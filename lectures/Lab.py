from Lab2 import Pet

class Cat(Pet):
    def __init__(self,*args,breed,**kwargs):
        super().__init__(*args,**kwargs)
        self.breed=breed

    def voice(self,phrase:str,nothing=0):
        print(f'Meow means {phrase}')
        nothing+=1
    
    def legacy_voise(self,*args,**kwargs):
        super().voice(*args,**kwargs)


pet1=Cat('Atmo',2,'red',breed='Main-coon 0.5')
print(f"breed={pet1.breed}")
pet1.voice('Meow')
pet1.setCount(12)
print(pet1.walk())
pet2=Cat('Turbo',3,'white',breed='Turkish Angora')
print(f"breed={pet2.breed}")
pet2.voice('Meow')
pet2.setCount(2)
print(pet2.walk())

pet2.legacy_voise('Bark')
