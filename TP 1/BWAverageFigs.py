import matplotlib.pyplot as plt
import ast

def getData(file):
    BW = open(file, "r")
    values = BW.read()
    BW.close()
    return values

def drawFig(Data):
    fig1, ax1 = plt.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(Data)
    plt.show()

def main():
    BW20800values = ast.literal_eval(getData("BW20800.txt"))
    BW31250values = ast.literal_eval(getData("BW31250.txt"))
    BW62500values = ast.literal_eval(getData("BW62500.txt"))
    BW125000values = ast.literal_eval(getData("BW1250000.txt"))
    BW500000values = ast.literal_eval(getData("BW500000.txt"))

    drawFig([BW20800values, BW31250values, BW62500values, BW125000values, BW500000values])

main()

