import random
print("This program will provide guesses for a number between 2 other numbers.")
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
guess = random.randrange(smaller, larger)
print("%d %d" % (smaller, larger))
print("Your number is %d" % (guess))
userinput = str(input("Enter =, <, or >: "))
count = 1
while userinput != "=":
    if userinput == "<":
        if guess - 1 < smaller:
            print("I'm out of guesses, and you cheated!")
            break
        else:
            larger = guess - 1
            count += 1
    if userinput == ">":
        if guess + 1 > larger:
            print("I'm out of guesses, and you cheated!")
            break
        else:
            smaller = guess + 1
            count += 1
    if smaller == larger:
        guess = smaller
    else:
        guess = random.randrange(smaller, larger)
    print("%d %d" % (smaller, larger))
    print("Your number is %d" % (guess))
    userinput = str(input("Enter =, <, or >: "))
else:
    print("Hooray, you've got it in %d tries!" % (count))
    print("Press enter to continue")
input()