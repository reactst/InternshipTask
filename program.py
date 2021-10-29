from klasa import *
b = Board()
while True:
    in_put = input("")
    if in_put.find("exit") != -1:
        print("EXITING")
        break
    lastPLACE = in_put.rfind("PLACE")
    firstPOS = in_put[lastPLACE + 6:lastPLACE + 9]
    values = firstPOS.split(',')
    b.x = int(values[0])
    b.y = int(values[1])
    novistr = in_put[lastPLACE+9:]
    if novistr.find("EAST")!=-1:
        b.f = 'E'
    elif novistr.find("WEST")!=-1:
        b.f = 'S'
    elif novistr.find("NORTH")!=-1:
        b.f = 'S'
    elif novistr.find("SOUTH") != -1:
        b.f = 'S'
    else:
        print("nesto nevalja")

    leftcnt = novistr.count("LEFT")
    for i in range(leftcnt):
        b.left()

    rightcnt = novistr.count("RIGHT")
    for i in range(rightcnt):
        b.right()

    movecnt = novi.count("MOVE")
    for i in range(movecnt):
        b.move()

    if novistr.find("REPORT")!=-1:
        b.report()
