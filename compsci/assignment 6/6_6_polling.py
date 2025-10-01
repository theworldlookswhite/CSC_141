# 6-6 try it yourself
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

take = {
    'jen',
    'erin',
    'edward', 
    'charlie'
}
for term in take:
    if term in favorite_languages:
        print(f'thank you for taking our poll {term}')
    else:
        print(f'{term} please take our poll')
