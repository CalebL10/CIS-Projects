import statistics

pop_size = int(input("Enter population size: "))
life_ex = float(input("Enter life expectancy: "))
sample_file = str(input("Enter sample file name: "))

file = open(sample_file, 'r')
mylist = []
for line in file:
    number = float(line)
    mylist.append(number)
file.close()

average_age_infected = statistics.mean(mylist)
r0 = life_ex / average_age_infected
hit = 1 - (1/r0)
doses = hit * pop_size

print("\nAverage age of infection: %.2f" % average_age_infected)
print("Base Reporoduction Number %.9f" % r0)
print("Herd Immunity Threshold: %.8f" % hit)
print("Doses Required: %.1f" % doses)

#Alternate way to format PRINT statements

#print(f"\nAverage age of infection: {average_age_infected:.2f}")
#print(f"Base Reporoduction Number: {r0:.9f}")
#print(f"Herd Immunity Threshold: {hit:.8f}")
#print(f"Doses Required: {doses:.1f}")