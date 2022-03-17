from xmlrpc.client import boolean


float = 1.0
interger = 2
string = 'three'
boolean = True

# pets = ['dog', 'cat', 'goldfish']
# faves=[x for x in pets if x == 'dog']
# print(faves)
# fave = next((x for x in pets if x == 'dog'), None)
# print(fave)
# fave = next((x for x in pets if x == 'horse'), None)
# print(fave)

dogs = {
    '1': {'name':'Noir', 'breed':'Schnoodle'},
    '2': {'name':'Bree', 'breed':'Mutt'},
    '3': {'name':'Bree', 'breed':'Retriever'},
    '4': {'name':'Duchess', 'breed':'Terrier'},
    '5': {'name':'Sparky', 'breed':'Mutt'}
}


# for x in dogs :
#     print(dogs[x]['breed'])

# mydogs = [dogs[x] for x in dogs if dogs[x]['breed'] == 'Mutt']  
# print(mydogs)  

def get_my_dogs(breed):
    return [dogs[x] for x in dogs if dogs[x]['breed'] == breed]

mydogs = get_my_dogs('Mutt')
print(mydogs)
mydogs = get_my_dogs('Retriever')
print(mydogs)

class Pet:
    def __init__(self, name, species, noise):
        self.name = name
        self.specises = species
        self.noise = noise
    
    def make_noise(self):
        print("I go " + self.noise)    

my_dog = Pet('Noir', 'dog', 'Woof!')
my_cat = Pet('Princess', 'cat', "Meow")

my_pets = [my_cat, my_dog]

my_cat.make_noise()
my_dog.make_noise()
print(my_dog.make_noise)
print(my_dog.__dict__['noise'])
print(my_cat.noise)
print(my_pets[0].noise)        