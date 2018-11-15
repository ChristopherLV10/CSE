import random

print("Lucky 7s!")
print("Round: 1")

playing = True
round = 1
money = 15
while money > 0:
    Dice_1 = random.randint(1, 6)
    Dice_2 = random.randint(1, 6)
    if Dice_1 + Dice_2 == 7:
        print("You win 4 dollars")
        round += 1
        print("Round:", round)
        money = money + 4
    else:
        print("You lose 1 dollar")
        round += 1
        print("Round:", round)
        money -= 1

    if money == 0:
        print("You ran out of money on Round", round)
        playing = False
