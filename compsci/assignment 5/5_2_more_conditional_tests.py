# 5-2 try it yourself
score = "90"
if score == '90':
    print("you win")
else: 
    print("not enough score")

score = "70"
if score == '90':
    print("you win")
else: 
    print("not enough score")

car = 'Ford'
car.lower() == 'ford'
print(car)

temperature = 100
humidity = 90
windspeed = 10
storm = (humidity > 70 or windspeed > 50) or (temperature < 32 and humidity > 60 and windspeed > 50)
storm = True

toppings = ['fudge', 'cherries', 'sprinkles', 'peanuts', 'brownie chunks']
'brownie chunks' in toppings