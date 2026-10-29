#Guessing Game
import random
def playgame():
    lucky_num=random.randint(1,50)
    while True:
        user_num=int(input("Guess the Luckey num:"))
        if user_num==lucky_num:
            print("You Won!")
            print("Game Over!")
            break
        elif user_num<lucky_num:
            print("Too Low")
        else:
            print("Too High")

    print("Thank You For Play")

print(playgame())