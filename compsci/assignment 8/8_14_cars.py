# 8-14 try it yourself
def carinfo(maker, model, **opt):
    cars = {
        'maker': maker,
        'model': model,
    }
    for opt, value in opt.items():
        cars[opt] = value
    
    return cars

mirage = carinfo('mitsubishi', 'mirage', year='2022', color='silver', cdplayer=False)
print(mirage)
corolla = carinfo('toyota', 'corolla', year='2003', color='blue', cdplayer=False )
print(corolla)
