import matplotlib.pyplot as plt
import json

def getData(file):
    with open(file, "r") as BW:
        values = json.loads(BW.read())
    # changing scale
    values = [int(x)/1000 for x in values]
    return values

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
    D10 = getData("DATA10.txt")
    D22 = getData("DATA22.txt")
    D43 = getData("DATA43.txt")

    drawFig([D10, D22, D43], [10, 22, 43])

main()

