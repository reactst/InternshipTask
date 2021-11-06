def setf (f):
    if f.find('EAST')!= -1:
        return 'EAST'
    elif f.find('WEST')!= -1:
        return 'WEST'
    elif f.find('NORTH')!= -1:
        return 'NORTH'
    elif f.find('SOUTH')!= -1:
        return 'SOUTH'
    else:
        return 'NEVALJA'
def move(x,y,f):
    if f == 'NORTH' and y < 5:
        y+=1
    if f == 'SOUTH' and y > 0:
        y-=1
    if f == 'EAST' and x < 5:
        x+=1
    if f == 'WEST' and x > 0:
        x-=1
    return x,y

def left(f):
    if f.find('NORTH')!=-1:
        nf = 'WEST'
    elif f.find('WEST')!=-1:
        nf = 'SOUTH'
    elif f.find('SOUTH')!=-1:
        nf = 'EAST'
    elif f.find('EAST')!=-1:
        nf = 'NORTH'
    return nf

def right(f):
    if f.find('NORTH')!=-1:
        nf = 'EAST'
    elif f.find('WEST')!=-1:
        nf = 'SOUTH'
    elif f.find('SOUTH')!=-1:
        nf = 'WEST'
    elif f.find('WEST')!=-1:
        nf = 'NORTH'
    return nf

def report (x,y,f):
    print (f'{x},{y},{f}')

while True:
    in_put = input('')
    if in_put.find('exit') != -1:
        print('EXITING')
        break
    input_list = in_put.split(' ')
    for i, v in enumerate(input_list):
        if v == 'PLACE':
            x = int(input_list[i+1].split(',')[0])
            y = int(input_list[i+1].split(',')[1])
            f = input_list[i+1].split(',')[2]
        if v == 'MOVE':
            x,y= move(x,y,f)
        if v == 'LEFT':
            f = left(f)
        if v == 'RIGHT':
            f = right(f)
        if v == 'REPORT':
            report(x,y,f)




