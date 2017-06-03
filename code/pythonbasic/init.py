class Animal:
    def __init__(self, **kwargs):
        self.species = kwargs.get("species")
        self.age = kwargs.get("age")
        self.sound = kwargs.get("sound")

class Animalattr:
    def __init__(self,**kwargs):
					for key, value in kwargs.items():
							setattr(self,key,value)
class Animalattrupdate:
    def __init__(self,**kwargs):
					self.__dict__.update(kwargs)
				