import csv

def getData(file_name):
    with open(file_name, mode='r') as logs:
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

def generateSecondDict(firstDict, numberOfMsgSent):
    dictio_average = {}
    for key in firstDict.keys():
        dictio_average[key] = firstDict[key]/numberOfMsgSent
    print("Average Doctionnary: ", dictio_average)
    print(len(dictio_average))
    return dictio_average

def generateAVG(secondDict, numberOfDevices):
    somme = 0
    
    for value in secondDict.values():
        somme = somme + float(value)
    return somme/numberOfDevices

def main():

    print("\n-----------------------------------------------------")
    print("1 - Pour SF = 7, Delay = 5s, 100 messages envoyes on a :")
    print("----------------------------------------------------- \n")

    data75100 = getData('log_sf7_5s_100.csv')
    nb_msg_recu_par_pers = generateFirstDict(data75100)
    avg_msg_par_pers = generateSecondDict(nb_msg_recu_par_pers, 100)
    average = generateAVG(avg_msg_par_pers, 21)
    print ("\n", average*100, "% des messages ont ete recus")


    print("\n-----------------------------------------------------")
    print("2 - Pour SF = 9, Delay = 5s, 30 messages envoyes on a :")
    print("----------------------------------------------------- \n")
    data9530 = getData('log_sf9_5s_30.csv')
    nb_msg_recu_par_pers = generateFirstDict(data9530)
    avg_msg_par_pers = generateSecondDict(nb_msg_recu_par_pers, 30)
    average = generateAVG(avg_msg_par_pers, 21)
    print ("\n", average*100, "% des messages ont ete recus")

    print("\n-----------------------------------------------------")
    print("3 - Pour SF = 11, Delay = 5s, 30 messages envoyes on a :")
    print("----------------------------------------------------- \n")
    data11530 = getData('log_sf11_5s_30.csv')
    nb_msg_recu_par_pers = generateFirstDict(data11530)
    avg_msg_par_pers = generateSecondDict(nb_msg_recu_par_pers, 30)
    average = generateAVG(avg_msg_par_pers, 21)
    print ("\n", average*100, "% des messages ont ete recus")

    print("\n-----------------------------------------------------")
    print("4 - Pour SF = 9, Delay = 1s, 30 messages envoyes on a :")
    print("----------------------------------------------------- \n")
    data11530 = getData('log_sf9_1s_30.csv')
    nb_msg_recu_par_pers = generateFirstDict(data11530)
    avg_msg_par_pers = generateSecondDict(nb_msg_recu_par_pers, 30)
    average = generateAVG(avg_msg_par_pers, 21)
    print ("\n", average*100, "% des messages ont ete recus")

    print("\n-----------------------------------------------------")
    print("5 - Pour SF = 9, Delay = 20s, 30 messages envoyes on a :")
    print("----------------------------------------------------- \n")
    data11530 = getData('log_sf9_20s_20.csv')
    nb_msg_recu_par_pers = generateFirstDict(data11530)
    avg_msg_par_pers = generateSecondDict(nb_msg_recu_par_pers, 20)
    average = generateAVG(avg_msg_par_pers, 21)
    print ("\n", average*100, "% des messages ont ete recus")
main()
