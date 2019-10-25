import csv

liste_arrivee = []

with open('log_sf7_5s_100.csv', mode='r') as logs:
    csv_reader = csv.reader(logs, delimiter=',')
    line_count = 0
    for row in csv_reader:
        var = (row[0])[7:]
        sender_number = var.split(":")[0]
        liste_arrivee.append(sender_number)
        line_count +=1
    print(line_count)
    # print(liste_arrivee)
    
dictio = {}
for sender in liste_arrivee:
    if sender in dictio:
        dictio[str(sender)] += 1
    else:
        dictio[str(sender)] = 1

dictio_average = {}

for key in dictio.keys():
    dictio_average[key] = dictio[key]/100

print(dictio_average)

dictio_all_average = {}

somme = 0
for value in dictio_average.values():
    somme = somme + float(value)

average = somme/21

print (average*100, "% des messages ont ete recus")
