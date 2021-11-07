def move(x, y, f):
    if f == 'NORTH' and y < 5:
        y += 1
    if f == 'SOUTH' and y > 0:
        y -= 1
    if f == 'EAST' and x < 5:
        x += 1
    if f == 'WEST' and x > 0:
        x -= 1
    return x, y

left = {
    'NORTH': 'WEST',
    'WEST': 'SOUTH',
    'SOUTH': 'EAST',
    'EAST': 'NORTH'
}

right = {
    'NORTH': 'EAST',
    'EAST': 'SOUTH',
    'SOUTH': 'WEST',
    'WEST': 'NORTH'
}

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
            if x < 0 or y < 0 or x > 5 or y >5:
                print (f'Invalid coordinates: {x}{y}')
                continue
            f = input_list[i+1].split(',')[2]
        if v == 'MOVE':
            x, y = move(x, y, f)
        if v == 'LEFT':
            f = left[f]
        if v == 'RIGHT':
            f = right[f]
        if v == 'REPORT':
            print(f'{x},{y},{f}')
