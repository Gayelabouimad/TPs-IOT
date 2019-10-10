import matplotlib.pyplot as plt
import ast

def getData(file):
    SF = open(file, "r")
    values = SF.read()
    SF.close()
    return values

def drawFig(Data):
    fig1, ax1 = plt.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(Data)
    plt.show()

def main():
    SF7values = ast.literal_eval(getData("SF7.txt"))
    SF9values = ast.literal_eval(getData("SF9.txt"))
    SF10values = ast.literal_eval(getData("SF10.txt"))

    drawFig([SF7values, SF9values, SF10values])

main()

