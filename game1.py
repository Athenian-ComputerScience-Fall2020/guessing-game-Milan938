#Collaborators: Megan
#Imports random numbers between the parameters the user inputs
import random
while True:

    first_num = int(input("Enter the lowest number: "))
    second_num = int(input("Enter the highest number: "))

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
                print("Try again, or press q to quit: ")
                a = input()
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
                    print("Try again, or press q to quit: ")
                    b = input()
                    if b == "q":
                        break
                    try:
                        b = int(b)
                        if b == y:
                            print("Congratulations, ", b, "was the right answer")
                        elif b > y:
                            print("Your guess of ", b, " was too high")
                        elif b < y:
                            print("Your guess of ", b, " was too small")
                    except:
                        print("Please enter an integer: ")
                    if b !=  y:
                        print("Try again, or press q to quit: ")
                        c = input()
                        if c == "q":
                            break
                        try:
                            c = int(c)
                            if c == y:
                                print("Congratulations, ", c, "was the right answer")
                            elif c > y:
                                print("Your guess of ", c, " was too high")
                            elif c < y:
                                print("Your guess of ", c, " was too small")
                        except:
                            print("Please enter an integer")

                        if c !=  y:
                            print("Try again, or press q to quit: ")
                            d = input()
                            if d == "q":
                                break
                            try:
                                d = int(d)
                                if d == y:
                                    print("Congratulations, ", d, "was the right answer")
                                elif d > y:
                                    print("Your guess of ", d, " was too high")
                                elif d < y:
                                    print("Your guess of ", d, " was too small")
                            except:
                                print("Please enter an integer")
                            if d != y:
                                print("Sorry, you're out of guesses")
                                break
#Cuts user off after too many guesses, or if they guess the right answer
    print("Thank you for playing, would you like to play again?")
    play_again = input("Yes or No: ")
    if play_again == "Yes":
        continue
    else:
        break
#Thank you message and option to play again or not