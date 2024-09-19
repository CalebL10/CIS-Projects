filename = input("Enter the file name: ")
f = open(filename, 'r')
print("\n%-15s%-10s%-10s" % ('Name', 'Hours', 'Total Pay'))
for line in f:
    linelist = line.split()
    name = str(linelist[0])
    wage = float(linelist[1])
    hours = int(linelist[2])
    total = hours * wage 
    print("%-15s%-10d%-10.2f" % (name, hours, total))

