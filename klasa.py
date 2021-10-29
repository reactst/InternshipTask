class Board:
    x, y = 0
    f = "N"

    def place(x, y, f):
        if f != "NORTH" or f != "EAST" or f != "WEST" or f != "SOUTH":
            return "invalid side"
        Board.x = x
        Board.y = y
        if f == "NORTH":
            Board.f = 'N'
        if f == "EAST":
            Board.f = 'E'
        if f == "WEST":
            Board.f = 'W'
        if f == "SOUTH":
            Board.f = 'S'

    def left():
        if Board.f == 'N':
            Board.f = 'W'
        elif Board.f == 'W':
            Board.f = 'S'
        elif Board.f == 'S':
            Board.f = 'E'
        elif Board.f == 'E':
            Board.f = 'N'
        else:
            return "something wrong"

    def right():
        if Board.f == 'N':
            Board.f = 'E'
        elif Board.f == 'E':
            Board.f = 'S'
        elif Board.f == 'S':
            Board.f = 'W'
        elif Board.f == 'W':
            Board.f = 'N'
        else:
            return "something2 wrong"

    def move():
        if Board.f == 'N' and Board.y < 5:
            Board.y += 1
        elif Board.f == 'N' and Board.y == 5:
            return "FALLING NORTH-IGNORING MOVEMENT"
        if Board.f == 'E' and Board.x < 5:
            Board.x += 1
        elif Board.f == 'E' and Board.x == 5:
            return "FALLING EAST-IGNORING MOVEMENT"
        if Board.f == 'S' and Board.x > 0:
            Board.f -= 1
        elif Board.f == 'S' and Board.x == 0:
            return "FALLING SOUTH-IGNORING MOVEMENT"
        if Board.f == 'W' and Board.x > 0:
            Board.x -= 1
        elif Board.f == 'W' and Board.x == 0:
            return "FALLING WEST-IGNORING MOVEMENT"

    def report():
        if Board.f == 'N':
            print(f'{Board.x},{Board.y},NORTH')
        if Board.f == 'E':
            print(f'{Board.x},{Board.y},EAST')
        if Board.f == 'S':
            print(f'{Board.x},{Board.y},SOUTH')
        if Board.f == 'W':
            print(f'{Board.x},{Board.y},WEST')
