# 6-10 try it yourself
numbers = {
    'silva': ['3', '222', '32'],
    'kiki': ['6', '24', '108'],
    'kel': ['18', '19', '20'],
    'mir': ['9', '5', '96'],
    'ron': ['7', '77', '777']
}
for name, numbers in numbers.items():
    print(f"\n{name} likes the numbers:")
    for number in numbers:
        print(f"{number}")