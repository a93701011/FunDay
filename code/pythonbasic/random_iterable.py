import random
def random_item(iterable):
    number = random.randint(0,len(iterable)-1)
    print(iterable[number])
random_item("treehouse") 
