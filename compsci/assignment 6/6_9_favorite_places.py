favoriteplaces = {
    'silva': ['north carolina', 'virginia', 'oddity expos'],
    'mir': ['thrift stores', 'home', 'local record stores'],
    'nathan': ['race tracks', 'washington', 'new hampshire'] 
}
for name, places in favoriteplaces.items():
    print(f"\n{name} likes to go to:")
    for place in places:
        print(f"{place}")