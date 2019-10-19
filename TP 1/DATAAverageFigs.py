import matplotlib.pyplot as plt
import ast

def getData(file):
    Data = open(file, "r")
    values = Data.read()
    Data.close()
    return values

def convertValuesToMilli(liste):
    newList = []
    for i in liste:
        newList.append(i/1000)
    return newList

def drawFig(Data, size):
    fig, axs = plt.subplots(2,2)

    # SF = 7
    axs[0, 0].set_title('BoxPlot for Size = '+ str(size[0]) + ' in Milliseconds', pad = 20)
    axs[0, 0].boxplot([Data[0],41.22], patch_artist = 'True',  labels =["Experimental" , "Theoretical"])

    # SF = 8
    axs[0, 1].set_title('BoxPlot for Size = '+ str(size[1]) + ' in Milliseconds', pad = 20)
    axs[0, 1].boxplot([Data[1], 56.58], patch_artist = 'True',  labels =["Experimental" , "Theoretical"])

    # SF = 9
    axs[1, 0].set_title('BoxPlot for Size = '+ str(size[2]) + ' in Milliseconds', pad = 20)
    axs[1, 0].boxplot([Data[2], 87.3], patch_artist = 'True',  labels =["Experimental" , "Theoretical"])

    fig.subplots_adjust(hspace=0.5, wspace=0.5)

    plt.show()

def main():
    D10 = ast.literal_eval(getData("DATA10.txt"))
    D22 = ast.literal_eval(getData("DATA22.txt"))
    D43 = ast.literal_eval(getData("DATA43.txt"))

    D10_scaled = convertValuesToMilli(D10)
    D22_scaled = convertValuesToMilli(D22)
    D43_scaled = convertValuesToMilli(D43)

    drawFig([D10_scaled, D22_scaled, D43_scaled], [10, 22, 43])

main()

