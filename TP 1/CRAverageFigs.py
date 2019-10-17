import matplotlib.pyplot as plt
import ast

def getData(file):
    CR = open(file, "r")
    values = CR.read()
    CR.close()
    return values

def convertValuesToMilli(liste):
    newList = []
    for i in liste:
        newList.append(i/1000)
    return newList

def drawFig(Data, CR):
    fig, axs = plt.subplots(2,2)

    # CR = 5
    axs[0, 0].set_title('BoxPlot for CR = '+ str(CR[0]) + ' in Milliseconds', pad = 20)
    axs[0, 0].boxplot([Data[0], 52.8] , patch_artist = 'True',  labels =["Experimental", "Theoritical" ])
  

    # CR = 6
    axs[0, 1].set_title('BoxPlot for CR = '+ str(CR[1]) + ' in Milliseconds', pad = 20)
    axs[0, 1].boxplot([Data[1], 63.74] , patch_artist = 'True',  labels =["Experimental", "Theoretical"])

    # CR = 7
    axs[1, 0].set_title('BoxPlot for CR = '+ str(CR[2]) + ' in Milliseconds', pad = 20)
    axs[1, 0].boxplot([Data[2], 70.91] , patch_artist = 'True',  labels =["Experimental", "Theoretical"])

    # CR = 8
    axs[1, 1].set_title('BoxPlot for CR = '+ str(CR[3]) + ' in Milliseconds', pad = 20)
    axs[1, 1].boxplot([Data[3], 78.08] , patch_artist = 'True',  labels =["Experimental", "Theoretical"])

    fig.subplots_adjust(hspace=0.6, wspace=0.6)

    plt.show()


def main():
    CR5values = ast.literal_eval(getData("CR5.txt"))
    CR6values = ast.literal_eval(getData("CR6.txt"))
    CR7values = ast.literal_eval(getData("CR7.txt"))
    CR8values = ast.literal_eval(getData("CR8.txt"))

    # changing scale```
    CR5values_scaled = convertValuesToMilli(CR5values)
    CR6values_scaled = convertValuesToMilli(CR6values)
    CR7values_scaled = convertValuesToMilli(CR7values)
    CR8values_scaled = convertValuesToMilli(CR8values)
    # print(SF7values_scaled)

    drawFig([CR5values_scaled, CR6values_scaled, CR7values_scaled, CR8values_scaled], [5 ,6 ,7, 8])

main()

