'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
import random

x = int(input("Guess a number from 1 to 20: "))
y = random.randint(0, 20)

if x == y:
        print("Congratulations, ", x, " was the right answer")
if x != y: 
    if x > y:
        print("Your guess of ", x, " was too high")
    elif x < y:
        print("Your guess of ", x, " was too small")

if x !=  y:
    a = int(input("Try again: "))
if a == y:
    print("Congratulations, ", a, "was the right answer")
if a > y:
    print("Your guess of ", a, " was too high")
if a < y:
    print("Your guess of ", a, " was too small")

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
