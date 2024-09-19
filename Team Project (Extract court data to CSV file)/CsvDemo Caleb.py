#create dictionaries
d1 = {"k1":"v1", "k2":"v2"}
d2 = {"k3":"v3", "k4":"v4"}

#create dictionary "d3" with both d1 and d2
d3 = dict(d1)
d3.update(d2)

import csv
FIELD_NAMES = ['first_name',
               'last_name',
               'status']

csvfile = open('names.csv', 'w', newline='')
writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES, extrasaction='ignore')

writer.writeheader()

data = {'first_name': 'Baked', 'last_name': 'Beans', 'status': 'tired', 'age': 109}
writer.writerow(data)
writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})