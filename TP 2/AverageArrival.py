import csv

def getData(file_name):
    with open('log_sf7_5s_100.csv', mode='r') as logs:
        liste_arrivee = []
        csv_reader = csv.reader(logs, delimiter=',')
        line_count = 0
        for row in csv_reader:
            var = (row[0])[7:]
            sender_number = var.split(":")[0]
            liste_arrivee.append(sender_number)
            line_count +=1
    return liste_arrivee

def generateFirstDict(data):
    dictio = {}
    for sender in data:
        if sender in dictio:
            dictio[str(sender)] += 1
        else:
            dictio[str(sender)] = 1
    return dictio

def generateSecondDict(firstDict):
    dictio_average = {}
    for key in firstDict.keys():
        dictio_average[key] = firstDict[key]/100

    return dictio_average

def generateThirdDict(secondDict):
    somme = 0
    for value in secondDict.values():
        somme = somme + float(value)
    return somme/21

def main():
    data = getData('log_sf7_5s_100.csv')
    nb_msg_recu_par_pers = generateFirstDict(data)
    avg_msg_par_pers = generateSecondDict(nb_msg_recu_par_pers)
    average = generateThirdDict(avg_msg_par_pers)
    print (average*100, "% des messages ont ete recus")

main()
