from klasa import *
b = Board()
while True:
    in_put = input("")
    if in_put.find("exit") != -1:
        print("EXITING")
        break
    lastPLACE = rfind("PLACE")
    firstPOS = in_put[lastPLACE + 6 : lastPLACE + 9]
    values = firstPOS.split(',')
    x = values[0]
    y = values[1]



