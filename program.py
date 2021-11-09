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
    shortened_list = input_list[(next(i for i in reversed(range(len(input_list))) if input_list[i] == 'PLACE')):]
    x = int(shortened_list[1].split(',')[0])
    y = int(shortened_list[1].split(',')[1])
    f = shortened_list[1].split(',')[2]
    for i, v in enumerate(shortened_list):
        if v == 'MOVE':
            x, y = move(x, y, f)
        if v == 'LEFT':
            f = left[f]
        if v == 'RIGHT':
            f = right[f]
        if v == 'REPORT':
            print(f'{x},{y},{f}')