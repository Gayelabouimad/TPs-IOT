import matplotlib.pyplot as plt
import ast

def getData(file):
    Data = open(file, "r")
    values = Data.read()
    Data.close()
    return values

def drawFig(Data):
    fig1, ax1 = plt.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(Data)
    plt.show()

def main():
    D10 = ast.literal_eval(getData("DATA10.txt"))
    D22 = ast.literal_eval(getData("DATA22.txt"))
    D43 = ast.literal_eval(getData("DATA43.txt"))

    drawFig([D10, D22, D43])

main()

