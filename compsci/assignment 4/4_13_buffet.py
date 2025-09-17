# 4-13 try it yourself
buffet_foods = ('pizza', 'pasta', 'beef', 'potatoes', 'vegetables')
for buffet_food in buffet_foods:
    print(f"this buffet offers {buffet_food}.") 
new_buffet_foods = ('chicken', 'pie', 'beef', 'potatoes', 'vegetables')
for new_buffet_food in new_buffet_foods:
    print(f"this buffet changed its menu. it now serves {new_buffet_food}")
buffet_foods[0] = 'chicken' # this is an intentional error