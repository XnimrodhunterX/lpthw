my_name = "Stephen Goldschmidt"
my_age = 43 # not a lie
my_height = 68.5 # inches
my_weight = 180 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = "Black"

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f'He\'s got {my_eyes} eyes and {my_height}')
print(f'His teeth are usually {my_teeth} depending on the coffee')

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")


print('dividing my weight by my age equals', my_weight / my_age)
print('let\'s round this to 3 digits', round(my_weight / my_age, 3))