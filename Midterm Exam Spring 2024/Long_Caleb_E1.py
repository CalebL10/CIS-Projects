#Written by Caleb Long
#Calculates average cost and age of inventory from a csv file and inputted COGS.

inv_file = str(input("Enter filename: "))
cogs = float(input("Enter cost of goods sold: "))
sum = 0
count = 0

file = open(inv_file, 'r')
for line in file:
    line = line.split(",")
    sum += float(line[1])
    count += 1
average_cost = sum / count
average_age = average_cost / cogs * 365

print("Average Cost of Inventory: %.2f" % average_cost)
print("Average Age of Inventory: %.2f" % average_age)