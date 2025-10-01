# 6-8 try it yourself
pets = []
pet = {'name': 'king',
           'species': 'dog',
           'age': '9',
           'owner': 'melissa'}
pets.append(pet)
pet = {'name': 'hans',
           'species': 'dog',
           'age': '7',
           'owner': 'kelly'}
pets.append(pet)
pet = {'name': 'dolly',
           'species': 'dog',
           'age': '16',
           'owner': 'matthew'}
pets.append(pet)
pet = {'name': 'marble',
           'species': 'cat',
           'age': '10',
           'owner': 'mirage'}
pets.append(pet)

for pet in pets:
    name = f"{pet['name']}"
    species = pet['species']
    age = pet['age']
    owner = pet['owner']
    print(f"{name} is a {species} owned by {owner} that is {age} years old.")