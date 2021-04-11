from matplotlib import colors
from matplotlib import pyplot as plt
import RushHour


def isGoalState(list):  ## 목표상태인지 확인하기
    if list[2][0] == 1:
        return True
    else:
        return False


def getcanmove(block):  ## 경계노드 출력 함수
    canmove = {"Red": [],
               "Blue": [],
               "Yellow": [],
               "Green": [],
               }
    for i in block:
        canmove[i.color] = RushHour.canmove(i)
    print("This was frontier node")
    print(canmove)
    return canmove


def queryStack(blocklist, data):  ## 문제 해결 함수
    query = []
    cmap = colors.ListedColormap(['White', 'Red', 'Blue', 'Yellow', 'Green', 'Brown', 'Orange'])
    for i in range(0, blocklist[0].x1):  ## 목표상태가 되도록 초기 스택 작성
        query.append([])
        query[i].append(blocklist[0].color)
        query[i].append("LEFT")
    while query is not None:
        if isGoalState(data):
            print("Goal State")
            break
        elif 1 < data[2][0] < 6:
            print("Can't Solve")
            break
        frontier = getcanmove(blocklist)
        if frontier.values() is None:
            print("Can't Solve")
            break
        dataset = []
        if "LEFT" in frontier["Red"]:
            data = blocklist[0].move("LEFT", data)
            query.pop()
            print("Popped")
            print("Query now : ", query)
        else:
            values = []
            index = []
            color = []
            scores = []
            count = 0
            for k in frontier.keys():
                colnum = 0
                for v in frontier[k]:
                    dataset.append(RushHour.resetandmove(blocklist[coltonum(k)], v))  ## 휴리스틱 값 계산을 위한 상태 저장
                    colnum = colnum + 1
                color.append(colnum)
            for n in range(0, len(dataset)):
                scores.append(getscore(dataset[n]))

            print("This was frontiers scores : ", scores)
            decision = max(scores)
            print("This was Selected scores : ", decision)
            for m in range(0, len(scores)):
                if scores[m] == decision:
                    count = m

            for o in range(0, 4):
                index.append(sum(color[0:o + 1]))

            for q in range(0, len(index) - 1):
                if index[q] <= count + 1 <= index[q + 1]:
                    break
            index.clear()

            for r in frontier.values():
                for s in r:
                    values.append(s)

            direction = values[count]

            query.append([])
            query[-1].append(blocklist[q + 1].color)  ##SelectedNode.color
            query[-1].append(direction)  ##SelectedNode.direction
            print("Added Query : ", query[-1][-2], query[-1][-1])
            query.pop()
            print("Popped")
            print("Query now : ", query)
            data = blocklist[q + 1].move(direction, data)

        plt.figure(figsize=(6, 6))
        plt.pcolor(data[::-1], cmap=cmap, edgecolors='k', linewidths=3)
        plt.show()


def coltonum(col):  ## 색깔을 blocklist의 index로 변환
    if col == "Red":
        return 0
    elif col == "Blue":
        return 1
    elif col == "Yellow":
        return 2
    elif col == "Green":
        return 3


def getscore(list):  ## 휴리스틱 함수 정의 h(x)
    score = 0
    scorepan = [[4, 5, 5, 6],  ## 각 위치별 점수
                [4, 5, 5, 5],
                [3, 2, 1, 0],
                [2, 1, 0, 0]]
    for i in range(0, 5):
        for j in range(0, 5):
            if list[i + 1][j + 1] == 0:
                score = score + scorepan[i][j]  ## 점수 계산

    return score


queryStack(RushHour.blocklist, RushHour.data)
print(getscore(RushHour.data))
