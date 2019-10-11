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
    CR5values = ast.literal_eval(getData("CR5.txt"))
    CR6values = ast.literal_eval(getData("CR6.txt"))
    CR7values = ast.literal_eval(getData("CR7.txt"))
    CR8values = ast.literal_eval(getData("CR8.txt"))

    drawFig([CR5values, CR6values, CR7values, CR8values])

main()

