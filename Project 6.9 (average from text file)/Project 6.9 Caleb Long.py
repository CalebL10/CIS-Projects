#Caleb Long Project 6.9

from functools import reduce

def main():
    filename = str(input("Enter Filename: "))
    sum = 0
    count = 0
    numbers = []

    file = open(filename, 'r')
    for line in file:
        numbers = numbers + line.split(" ")

    numbers = list(map(float, numbers))

    count = len(numbers)
    sum = reduce(lambda x,y: x + y, numbers)

    average = sum / count

    print("The average of the numbers in the file is: %2.2f" % (average))

main()