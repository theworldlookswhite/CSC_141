# temperature = 60

# if temperature > 90:
   # print("its hot")
# elif temperature > 70:
   # print("its warm today")
# elif temperature > 50:
   # print("its a little chilly")
# else: 
    # print("its a little cold")

temperature = 100
humidity = 90
windspeed = 10
storm = (humidity > 70 or windspeed > 50) or (temperature < 32 and humidity > 60 and windspeed > 50)
storm = True
print(storm)

if storm:
    print("theres a serious storm")
else: 
    print("its mild right now")

animals = ["cat", "cow", "dog"]
if animals: 
    print("there are animals")
animals.pop()
animals.pop()
animals.pop()
if animals:
    print("there are animals")
else: 
    print("there are no animals")

print("are you providing celsius (c) or fahrenheit (f)")
scale = input()
scale = scale.lower
print("how many degrees")
degrees = input()
degrees = int(degrees)

if scale == ("c"):
    fahrenheit = (degrees * 9 / 5) + 32
    print(fahrenheit)
elif scale =="f":
    celsius = (degrees - 32) * (5 / 9)
    print(celsius)
else: 
    print("not a valid scale")
#  °C = (°F − 32) x 5/9 
# °F = (°C × 9/5) + 32 