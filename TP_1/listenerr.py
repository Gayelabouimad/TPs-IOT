import serial #Serial imported for Serial communication
import time #Required to use delay functions

def initialize() :
    ArduinoSerial = serial.Serial('com4',115200)
    time.sleep(2)
    return ArduinoSerial

def read(ArduinoSerial, liste1):
    a = ArduinoSerial.readline()
    liste1.append(int(a.decode().replace("\r\n", "")))
    return liste1

def main():
    AS = initialize()
    print("initialized")
    liste1 = []
    i = 0
    print("listening")
    while (i< 100):
        print(".\n")
        liste1 = read(AS, liste1)
        i += 1
    f = open("BW31250.txt", "w")
    f.write(str(liste1))
    f.close()
    print(liste1)


main()
