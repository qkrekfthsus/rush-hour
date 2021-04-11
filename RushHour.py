import copy

import numpy as np
from matplotlib import colors
from matplotlib import pyplot as plt
import blockinfo


########################## 초기 상태 ####################################

blocklist = []


def getcolor(number):
    if number == 1:
        return "Red"
    elif number == 2:
        return "Blue"
    elif number == 3:
        return "Yellow"
    elif number == 4:
        return "Green"


def CanMakeBlock(list, y, x):
    canmake = []
    if list[y][x - 1] == 0:
        canmake.append("LEFT")
    if list[y][x + 1] == 0:
        canmake.append("RIGHT")
    if list[y - 1][x] == 0:
        canmake.append("UP")
    if list[y + 1][x] == 0:
        canmake.append("DOWN")
    return canmake


def RandomBlockCreate(list, number):
    if number == 1:
        x = np.random.randint(2, 4)
        list[2][x] = number
        list[2][x + 1] = number
        blocklist.append(blockinfo.Block(2, x, 2, x + 1, getcolor(number)))
    else:
        x = np.random.randint(1, 5)
        y = np.random.randint(1, 5)
        value = list[y][x]
        if value == 0:
            blockmake = CanMakeBlock(list, y, x)
            if len(blockmake) == 0:
                RandomBlockCreate(list, number)
            else:
                str = blockmake[np.random.randint(0, len(blockmake))]
                if str == "UP":
                    blocklist.append(blockinfo.Block(y - 1, x, y, x, getcolor(number)))
                    list[y][x] = number
                    list[y - 1][x] = number
                elif str == "DOWN":
                    blocklist.append(blockinfo.Block(y, x, y + 1, x, getcolor(number)))
                    list[y][x] = number
                    list[y + 1][x] = number
                elif str == "LEFT":
                    blocklist.append(blockinfo.Block(y, x - 1, y, x, getcolor(number)))
                    list[y][x - 1] = number
                    list[y][x] = number
                elif str == "RIGHT":
                    blocklist.append(blockinfo.Block(y, x, y, x + 1, getcolor(number)))
                    list[y][x] = number
                    list[y][x + 1] = number
        else:
            RandomBlockCreate(list, number)
    return list


data = [[5, 5, 5, 5, 5, 5],     ## 초기 상태
        [5, 0, 0, 0, 0, 5],
        [6, 0, 0, 0, 0, 5],
        [5, 0, 0, 0, 0, 5],
        [5, 0, 0, 0, 0, 5],
        [5, 5, 5, 5, 5, 5]]

for i in range(1, 5):
    data = RandomBlockCreate(data, i)


def resetandmove(block, str):   ## 경계노드에 추가를 위한 블록 움직임 함수
    list = copy.deepcopy(data)
    cblock = copy.deepcopy(block)
    if str == "UP":
        temp = list[cblock.y1][cblock.x1]
        list[cblock.y2][cblock.x2] = 0
        cblock.y1 = cblock.y1 - 1
        cblock.y2 = cblock.y2 - 1
        list[cblock.y1][cblock.x1] = temp
        list[cblock.y2][cblock.x2] = temp
    elif str == "DOWN":
        temp = list[cblock.y2][cblock.x2]
        list[cblock.y1][cblock.x1] = 0
        cblock.y1 = cblock.y1 + 1
        cblock.y2 = cblock.y2 + 1
        list[cblock.y1][cblock.x1] = temp
        list[cblock.y2][cblock.x2] = temp
    elif str == "LEFT":
        temp = list[cblock.y1][cblock.x1]
        list[cblock.y2][cblock.x2] = 0
        cblock.x1 = cblock.x1 - 1
        cblock.x2 = cblock.x2 - 1
        list[cblock.y1][cblock.x1] = temp
        list[cblock.y2][cblock.x2] = temp
    elif str == "RIGHT":
        temp = list[cblock.y1][cblock.x1]
        list[cblock.y1][cblock.x1] = 0
        cblock.x1 = cblock.x1 + 1
        cblock.x2 = cblock.x2 + 1
        list[cblock.y1][cblock.x1] = temp
        list[cblock.y2][cblock.x2] = temp
    return list


def canmove(block, list=data):  ## 움직일 수 있는 값들을 저장하는 함수
    cblock = copy.deepcopy(block)
    direction = []
    if cblock.getDirect() == "Y":
        if list[cblock.y1 - 1][cblock.x1] == 0:
            direction.append("UP")
        if list[cblock.y2 + 1][cblock.x1] == 0:
            direction.append("DOWN")
    elif cblock.getDirect() == "X":
        if list[cblock.y1][cblock.x1 - 1] == 0 or list[cblock.y1][cblock.x1 - 1] == 6:
            direction.append("LEFT")
        if list[cblock.y1][cblock.x2 + 1] == 0:
            direction.append("RIGHT")
    return direction


cmap = colors.ListedColormap(['White', 'Red', 'Blue', 'Yellow', 'Green', 'Brown', 'Orange'])    ## 리스트컬러맵

plt.figure(figsize=(6, 6))
plt.pcolor(data[::-1], cmap=cmap, edgecolors='k', linewidths=3)
plt.show()

