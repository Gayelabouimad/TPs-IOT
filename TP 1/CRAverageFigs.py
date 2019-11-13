import matplotlib.pyplot as plt
import json

def getData(file):
    with open(file, "r") as BW:
        values = json.loads(BW.read())
    # changing scale
    values = [int(x)/1000 for x in values]
    return values

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
    CR5values = getData("CR5.txt")
    CR6values = getData("CR6.txt")
    CR7values = getData("CR7.txt")
    CR8values = getData("CR8.txt")

    # print(SF7values_scaled)

    drawFig([CR5values, CR6values, CR7values, CR8values], [5 ,6 ,7, 8])

main()

