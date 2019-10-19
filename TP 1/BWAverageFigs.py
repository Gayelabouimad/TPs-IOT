import matplotlib.pyplot as plt
import ast

def getData(file):
    BW = open(file, "r")
    values = BW.read()
    BW.close()
    return values

def convertValuesToMilli(liste):
    newList = []
    for i in liste:
        newList.append(i/1000)
    return newList

def drawFig(Data, BW):
    fig, axs = plt.subplots(3,2)

    # BW = 20800
    axs[0, 0].set_title('BoxPlot for BW = '+ str(BW[0]) + ' in Milliseconds', pad = 20)
    axs[0, 0].boxplot([Data[0], 340] , patch_artist = 'True',  labels =["Experimental", "Theoretical"])

    # BW = 31250
    axs[0, 1].set_title('BoxPlot for BW = '+ str(BW[1]) + ' in Milliseconds', pad = 20)
    axs[0, 1].boxplot([Data[1], 226.3], patch_artist = 'True',  labels =["Experimental" , "Theoretical"])

    # BW = 62500
    axs[1, 0].set_title('BoxPlot for BW = '+ str(BW[2]) + ' in Milliseconds', pad = 20)
    axs[1, 0].boxplot([Data[2], 113.15], patch_artist = 'True',  labels =["Experimental", "Theoretical"])

    # BW = 125000
    axs[1, 1].set_title('BoxPlot for BW = '+ str(BW[3]) + ' in Milliseconds', pad = 20)
    axs[1, 1].boxplot([Data[3], 56.58], patch_artist = 'True',  labels =["Experimental", "Theoretical"])

    # BW = 500000
    axs[2, 0].set_title('BoxPlot for BW = '+ str(BW[4]) + ' in Milliseconds', pad = 20)
    axs[2, 0].boxplot([Data[4], 14.14],  patch_artist = 'True',  labels =["Experimental", "Theoretical"])
    fig.subplots_adjust(hspace=0.7, wspace=0.7)

    plt.show()

def main():
    BW20800values = ast.literal_eval(getData("BW20800.txt"))
    BW31250values = ast.literal_eval(getData("BW31250.txt"))
    BW62500values = ast.literal_eval(getData("BW62500.txt"))
    BW125000values = ast.literal_eval(getData("BW125000.txt"))
    BW500000values = ast.literal_eval(getData("BW500000.txt"))

    # changing scale```
    BW20800values_scaled = convertValuesToMilli(BW20800values)
    BW31250values_scaled = convertValuesToMilli(BW31250values)
    BW62500values_scaled = convertValuesToMilli(BW62500values)
    BW125000values_scaled = convertValuesToMilli(BW125000values)
    BW500000values_scaled = convertValuesToMilli(BW500000values)

    drawFig([BW20800values_scaled, BW31250values_scaled, BW62500values_scaled, BW125000values_scaled, BW500000values_scaled], [20800, 31250, 62500, 125000, 500000])

main()

