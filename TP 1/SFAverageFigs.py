import matplotlib.pyplot as plt
import json

def getData(file):
    with open(file, "r") as BW:
        values = json.loads(BW.read())
    # changing scale
    values = [int(x)/1000 for x in values]
    return values

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
    SF7values = getData("SF7.txt")
    SF9values = getData("SF9.txt")
    SF10values = getData("SF10.txt")

    print(SF7values)

    drawFig([SF7values, SF9values, SF10values], [7 ,9 ,10])

main()

