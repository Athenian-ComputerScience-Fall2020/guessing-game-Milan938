#Collaborators: Megan

import random
while True:

    first_num = int(input("Enter the lowest number: "))
    second_num = int(input("Enter the second number: "))

    print("Guess a number from ", first_num, " to ", second_num)
    x = int(input())
    y = random.randint(first_num, second_num)

    while True:
        if x == y:
            print("Congratulations, ", x, " was the right answer")
        if x != y: 
            if x > y:
                print("Your guess of ", x, " was too high")
            elif x < y:
                print("Your guess of ", x, " was too small")

        if x !=  y:
            a = input("Try again, or press q to quit: ")
            if a == "q":
                break
            try:
                a = int(a)
                if a == y:
                    print("Congratulations, ", a, "was the right answer")
                elif a > y:
                    print("Your guess of ", a, " was too high")
                elif a < y:
                    print("Your guess of ", a, " was too small")
            except:
                print("Please enter an integer")
        if a !=  y:
            b = int(input("Try again: "))
            if b == y:
                print("Congratulations, ", b, "was the right answer")
            if b > y:
                print("Your guess of ", b, " was too high")
            if b < y:
                print("Your guess of ", b, " was too small")

        if b !=  y:
            c = int(input("Try again: "))
            if c == y:
                print("Congratulations, ", c, "was the right answer")
            if c > y:
                print("Your guess of ", c, " was too high")
            if c < y:
                print("Your guess of ", c, " was too small")

        if c !=  y:
            d = int(input("Try again: "))
            if d == y:
                print("Congratulations, ", d, "was the right answer")
            if d > y:
                print("Your guess of ", d, " was too high")
            if d < y:
                print("Your guess of ", d, " was too small")

        if d != y:
            print("Sorry, you're out of guesses")
            break

    print("Thank you for playing, would you like to play again?")
    play_again = input("Yes or No: ")
    if play_again == "Yes":
        continue
    else:
        break