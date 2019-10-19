import matplotlib.pyplot as plt
import ast

def getData(file):
    SF = open(file, "r")
    values = SF.read()
    SF.close()
    return values

def convertValuesToMilli(liste):
    newList = []
    for i in liste:
        newList.append(i/1000)
    return newList

def drawFig(Data, SF):
    fig, axs = plt.subplots(2,2)

    # SF = 7
    axs[0, 0].set_title('BoxPlot for SF = '+ str(SF[0]) + ' in Milliseconds', pad = 20)
    axs[0, 0].boxplot([Data[0],56.58], patch_artist = 'True',  labels =["Experimental" , "Theoretical"])

    # SF = 8
    axs[0, 1].set_title('BoxPlot for SF = '+ str(SF[1]) + ' in Milliseconds', pad = 20)
    axs[0, 1].boxplot([Data[1], 205.82], patch_artist = 'True',  labels =["Experimental" , "Theoretical"])

    # SF = 9
    axs[1, 0].set_title('BoxPlot for SF = '+ str(SF[2]) + ' in Milliseconds', pad = 20)
    axs[1, 0].boxplot([Data[2],370.69], patch_artist = 'True',  labels =["Experimental" , "Theoretical"])

    fig.subplots_adjust(hspace=0.5, wspace=0.5)

    plt.show()

def main():
    SF7values = ast.literal_eval(getData("SF7.txt"))
    SF9values = ast.literal_eval(getData("SF9.txt"))
    SF10values = ast.literal_eval(getData("SF10.txt"))

    # changing scale```
    SF7values_scaled = convertValuesToMilli(SF7values)
    SF9values_scaled = convertValuesToMilli(SF9values)
    SF10values_scaled = convertValuesToMilli(SF10values)
    print(SF7values_scaled)

    drawFig([SF7values_scaled, SF9values_scaled, SF10values_scaled], [7 ,9 ,10])

main()

