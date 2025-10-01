# 6-7 try it yourself
people = []
person = {'firstname': 'silva',
           'lastname': 'wisenburk',
           'age': '18',
           'location': 'north carolina'}
people.append(person)
person = {'firstname': 'charlie',
           'lastname': 'emily',
           'age': '19',
           'location': 'utah'}
people.append(person)
person = {'firstname': 'henry',
           'lastname': 'miller',
           'age': '30',
           'location': 'california'}
people.append(person)
for person in people:
    name = f"{person['firstname']} {person['lastname']}"
    age = person['age']
    location = person['location']
    print(f"{name} is {age} years old and lives in {location}")
