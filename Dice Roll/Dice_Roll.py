import random

min_val = 1
max_val = 6

print("Rolling The Dices...")

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("The Values are :")
    
    first_dice=random.randint(min_val, max_val)
    print(first_dice)
    
    second_dice=random.randint(min_val, max_val)
    print(second_dice)

    if(first_dice==6 and second_dice == 6):
        print("Rolling The Dices Again...")
        roll_again="yes"
    else:
        print("No More Rolling")
        roll_again="n"
