# def indexofsqueres(x, y):
#     listofx = [0,1,2,3,4,6,7,8,9]
#     listofy = [0,1,2,3,4,6,7,8,9]
#     startx = listofx[x] * 72
#     starty = listofy[y] * 72
#     return startx, starty
#
# print(indexofsqueres(1, 0))


table1 =[[2,0,1,0,0,1,0,0,0,0],
        [0,0,1,0,0,1,1,1,0,1],
        [0,1,0,0,0,1,1,1,0,1],
        [0,1,0,0,0,1,0,0,0,1],
        [0,1,1,1,1,1,0,1,0,1],
        [0,0,0,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,1,0,1],
        [1,1,0,0,0,1,1,1,0,1],
        [1,1,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,1,1,1,0,1]]

print(table1[0])

def creatmapvalues(table):
    mapvalues = []
    for i in range(len(table)):
        for j in range(len(table)):
            mapplace = {}
            mapplace['x'] = j
            mapplace['y'] = i
            if table[i][j] == 0:
                mapplace['type'] = 'floor'
            elif table[i][j] == 1:
                mapplace['type'] = 'wall'
            elif table[i][j] == 2:
                mapplace['type'] = 'hero'
            mapvalues.append(mapplace)
    return mapvalues

print creatmapvalues(table1)
