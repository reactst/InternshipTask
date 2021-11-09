class Table:
     
    def __init__(self,x,y,f):
        self.x = int(x)
        self.y = int(y)
        self.f = f
        self.leftr = {
        'NORTH': 'WEST',
        'WEST': 'SOUTH',
        'SOUTH': 'EAST',
        'EAST': 'NORTH'
        }
        self.rightr = {
        'NORTH': 'EAST',
        'EAST': 'SOUTH',
        'SOUTH': 'WEST',
        'WEST': 'NORTH'
        }

    def move(self):
        if self.f == 'NORTH' and self.y < 5:
            self.y += 1
        elif self.f == 'SOUTH' and self.y > 0:
            self.y -= 1
        elif self.f == 'EAST' and self.x < 5:
            self.x += 1
        elif self.f == 'WEST' and self.x > 0:
            self.x -= 1

    def left (self):
        self.f = self.leftr[self.f]
    
    def right (self):
        self.f = self.rightr[self.f]
    
    
    def report (self):
        print(f'{self.x},{self.y},{self.f}')

while True:
    in_put = input('')
    input_list = in_put.split(' ')
    shortened_list = input_list[(next(i for i in reversed(range(len(input_list))) if input_list[i] == 'PLACE')):]
    koordinate = shortened_list[1].split(',')
    t = Table(koordinate[0],koordinate[1],koordinate[2])
    for i, v in enumerate(shortened_list):
        if v == 'MOVE':
            t.move()
        elif v == 'LEFT':
            t.left()
        elif v == 'RIGHT':
            t.right()
        elif v == 'REPORT':
            t.report()