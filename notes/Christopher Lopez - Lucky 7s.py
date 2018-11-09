import random


Dice_1 = random.randint(1, 6)
Dice_2 = random.randint(1, 6)

print("Lucky 7s!")
print("Round: 1")

round = 1
money = 15

if Dice_1 + Dice_2 == 7:
     print("You win 4 dollars")
     round = round + 1
     print("Round:",round)
     money = money + 4
else:
     print("You lose 1 dollar")
     round = round + 1
     print("Round:",round)
     money = money - 1
