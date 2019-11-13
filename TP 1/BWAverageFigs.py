import matplotlib.pyplot as plt
import json

def getData(file):
    with open(file, "r") as BW:
        values = json.loads(BW.read())
    # changing scale
    values = [int(x)/1000 for x in values]
    return values

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
    BW20800values = getData("BW20800.txt")
    BW31250values = getData("BW31250.txt")
    BW62500values = getData("BW62500.txt")
    BW125000values = getData("BW125000.txt")
    BW500000values = getData("BW500000.txt")

    drawFig([BW20800values, BW31250values, BW62500values, BW125000values, BW500000values], [20800, 31250, 62500, 125000, 500000])

main()

