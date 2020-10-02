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
            b = input("Try again, or press q to quit: ")
            if a == "q":
                break
            try:
                b = int(b)
                if b == y:
                    print("Congratulations, ", b, "was the right answer")
                if b > y:
                    print("Your guess of ", b, " was too high")
                if b < y:
                    print("Your guess of ", b, " was too small")
            except:
                print("Please enter an integer: ")
        if b !=  y:
            c = input("Try again, or press q to quit: ")
            if c == "q":
                break
            try:
                c = int(a)
                if a == y:
                    print("Congratulations, ", a, "was the right answer")
                elif c > y:
                    print("Your guess of ", a, " was too high")
                elif c < y:
                    print("Your guess of ", a, " was too small")
            except:
                print("Please enter an integer")

        if c !=  y:
            d = input("Try again, or press q to quit: ")
            if d == "q":
                break
            try:
                d = int(a)
                if d == y:
                    print("Congratulations, ", a, "was the right answer")
                elif d > y:
                    print("Your guess of ", a, " was too high")
                elif d < y:
                    print("Your guess of ", a, " was too small")
            except:
                print("Please enter an integer")
        if d != y:
            print("Sorry, you're out of guesses")
            break

    print("Thank you for playing, would you like to play again?")
    play_again = input("Yes or No: ")
    if play_again == "Yes":
        continue
    else:
        break